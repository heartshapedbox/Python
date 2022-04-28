
import os
# changing CWD
os.chdir("D:\Code\Python\Scraping\lesson1")
import requests
import re

# import BeautifulSoup
from bs4 import BeautifulSoup

# read .html file
with open("index.html", encoding="utf8") as file:
    text = file.read()

#parse .html file
soup = BeautifulSoup(text, "lxml")

#get all links
list_ref = soup.find_all("a")
def get_links(n):
    for i in range(len(n)):
        n[i] = n[i].get("href")
    text = "\n".join(str(i) for i in n)
    return text

#get all h3
list_h3 = soup.find_all("h3")
def get_h3_string(n):
    for i in range(len(n)):
        n[i] = n[i].string.strip()
    text = "\n".join(str(i) for i in n)
    return text

#get all post__text
list_post = soup.find_all("div", class_="post__text")
def get_posts_string(n):
    for i in range(len(n)):
        n[i] = n[i].string.strip()
    text = "\n".join(str(i) for i in n)
    return text

#get all user_info
user_info = soup.find(class_="user__info").find_all("span")
def get_user_info(n):
    for i in range(len(n)):
        n[i] = n[i].string
    text = "\n".join(str(i) for i in n)
    return text

#get all links with string
links = soup.find_all("a")
def get_links_with_string(n):
    obj_list = [0 for i in n]
    for i in range(len(n)):
        link_url = n[i].get("href")
        link_name = n[i].string
        obj_list[i] = (f"{link_name}: {link_url}")
    text = "\n".join(str(i) for i in obj_list)
    return text

#get all post with post_h3 and post_string
post_h3 = soup.find_all("h3")
post_string = soup.find_all(class_="post__text")
def get_post_h3_with_string(n,m):
    obj_list = [0 for i in n]
    for i in range(len(n)):
        obj_list[i] = (f"{n[i].string.strip()}\n {m[i].string.strip()}\n")
    text = "\n".join(str(i) for i in obj_list)
    return text

#get all attributes from tag "other__links"
other_links = soup.find(class_="some__links").find_all("a")
def get_all_attrs(n):
    obj_list = [0 for i in n]
    for i in range(len(n)):
        a = n[i].get("href")
        b = n[i].get("data-attr")
        obj_list[i] = a, b
    text1 = "\n".join(str(i) for i in obj_list[0])
    text2 = "\n".join(str(i) for i in obj_list[1])
    return text1 + "\n" + text2

#get all texts with "the" articles inside using re
all_the = soup.find_all(string=re.compile("the"))
def get_all_the_articles(n):
    for i in range(len(n)):
        n[i] = n[i].strip()
    text = "\n".join(str(i) for i in n)
    return text

print(get_all_the_articles(all_the))
