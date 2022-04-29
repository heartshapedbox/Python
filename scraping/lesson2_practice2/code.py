import os
os.chdir("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\data")
import re
import requests
import csv
import json
import random
from random import randrange
from time import sleep
from bs4 import BeautifulSoup

url="https://www.hsnstore.eu/"
headers={
    "access-control-allow-credentials": "true",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36"
}

request=requests.get(url,headers=headers)
webpage=request.text

with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\index.html", "w", encoding="utf-8") as file:
    file.write(webpage)
with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\index.html", encoding="utf-8") as file:
    webpage_text=file.read()

soup=BeautifulSoup(webpage_text, "lxml")

categories_list={}
sub_categories_list={}

categories_list_names_and_links=soup.find("div", class_="menucontainer").find_all("li", class_="first-lvl")
sub_categories_list_names_and_links=soup.find("div", class_="menucontainer").find_all("li", class_="second-lvl")

for i in categories_list_names_and_links:
    category_name=i.a.string
    category_url=i.a.get("href")
    rep=[" ","-",", ","/"]
    for i in rep:
        if i in category_name:
            category_name=category_name.replace(i, "_")
    categories_list[(f"{category_name}")]=category_url

for i in sub_categories_list_names_and_links:
    sub_category_name=i.a.string
    sub_category_url=i.a.get("href")
    rep=[" ","-",", ","/"]
    for i in rep:
        if i in sub_category_name:
            sub_category_name=sub_category_name.replace(i, "_")
    sub_categories_list[(f"{sub_category_name}")]=sub_category_url

with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\categories_list.json", "w", encoding="utf-8") as file:
    json.dump(categories_list, file, indent=4, ensure_ascii=False)
with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\sub_categories_list.json", "w", encoding="utf-8") as file:
    json.dump(sub_categories_list, file, indent=4, ensure_ascii=False)
with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\sub_categories_list.json", encoding="utf-8") as file:
    sub_cat_list=json.load(file)

actions=int(len(sub_cat_list))
print(f"Total actions: {actions}\n")

count=0
for sub_category_name, sub_category_url in sub_cat_list.items():
    request=requests.get(url=sub_category_url,headers=headers)
    webpage=request.text

    with open(f"{count}_{sub_category_name}.html", "w", encoding="utf-8") as file:
        file.write(webpage)
    with open(f"{count}_{sub_category_name}.html", encoding="utf-8") as file:
        webpage_text=file.read()
    with open(f"{count}_{sub_category_name}.csv", "w", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(
            (
                "Product_name",
                "Product_series",
                "Product_image",
                "Product_page",
                "Product_description",
                "Product_price"
            )
        )

    soup=BeautifulSoup(webpage_text, "lxml")

    product_data=[]
    products_data=soup.find_all(class_="col-xs-12 col-sm-7 product_list_detailed_box")

    for i in products_data:
        product_name=i.a.div.next_sibling.next_sibling.string.strip()
        product_series=i.a.div.string.strip()
        product_page=i.a.get("href")
        try:
            product_description=i.a.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string.strip()
        except AttributeError:
            pass
            product_description=None

        product_image=i.parent.previous_sibling.previous_sibling.a.img.get("data-src")

        try:
            product_price=i.next_sibling.next_sibling.div.div.div.div.next_sibling.next_sibling.string.strip()
        except AttributeError:
            pass
            product_price=None

        product_data.append(
            {
                "Product_name": product_name,
                "Product_series": product_series,
                "Product_image": product_image,
                "Product_page": product_page,
                "Product_description": product_description,
                "Product_price": product_price
            }
        )

        with open(f"{count}_{sub_category_name}.json", "w", encoding="utf-8") as file:
            json.dump(product_data, file, indent=4, ensure_ascii=False)
        with open(f"{count}_{sub_category_name}.csv", "a", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(
                (
                    product_name,
                    product_series,
                    product_image,
                    product_page,
                    product_description,
                    product_price
                )
            )

    count+=1
    print(f"Action #:{count}. Category: {sub_category_name}")
    actions-=1
    if actions==0:
        print(f"Status: Complete!")
        break
    print(f"Actions remain: {actions}")
    sleep(random.randrange(2, 5))
