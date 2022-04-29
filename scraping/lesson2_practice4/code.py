import os
os.chdir("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\data")
import re
import requests
import csv
import json
import random
from random import randrange
from time import sleep
from bs4 import BeautifulSoup



url="https://99designs.com/discover?category=logo-design"
headers={
    "access-control-allow-credentials": "true",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Mobile Safari/537.36"
}

def get_pages_urls():
    pages_urls={}
    page_number=1
    for i in range(1,101):
        page_url="https://99designs.com/discover?category=logo-design"
        page_url+=f"&page={i}"
        if "=0" in page_url:
            page_url=page_url.replace("=0", "")
        pages_urls[f"Page #{page_number}"]=page_url
        page_number+=1

    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\pages_urls.json", "a", encoding="utf-8") as file:
        json.dump(pages_urls, file, indent=4, ensure_ascii=False)
get_pages_urls()


def get_cards_urls():
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\pages_urls.json", encoding="utf-8") as file:
        pgs_urls=json.load(file)

    html_number=1
    cards_urls={}
    for page_number, page_url in pgs_urls.items():
        request=requests.get(page_url, headers=headers)
        webpage=request.text

        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\data\\Page_{html_number}.html", "w", encoding="utf-8") as file:
            file.write(webpage)
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\data\\Page_{html_number}.html", encoding="utf-8") as file:
            webpage_text=file.read()
        soup=BeautifulSoup(webpage_text, "lxml")
        look_for_cards_urls=soup.find_all(class_="mediabox mediabox--linked")

        card_number_on_page=1
        for i in look_for_cards_urls:
            card_url="https://99designs.com"+i.a.get("href")
            cards_urls[card_url]=card_number_on_page
            with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\cards_urls.json", "w", encoding="utf-8") as file:
                json.dump(cards_urls, file, indent=4, ensure_ascii=False)
            card_number_on_page+=1
        html_number+=1
get_cards_urls()


def get_cards_data():
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\pages_urls.json", encoding="utf-8") as file:
        pgs_urls=json.load(file)
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice4_pages\\cards_urls.json", encoding="utf-8") as file:
        crds_urls=json.load(file)

    pages_quantity=int(len(pgs_urls))
    print(f"Total number of pages: {pages_quantity}")
    cards_quantity=int(len(crds_urls))
    print(f"Total number of cards: {cards_quantity}\n")

    page_num=1
    for page_number, page_url in pgs_urls.items():
        with open(f"Page_{page_num}.csv", "w", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(
                (
                    "Card_title",
                    "Card_ID",
                    "Card_image",
                    "Card_url",
                    "Card_user_profile",
                    "Card_user_name",
                    "Card_user_avatar",
                    "Card_likes"
                )
            )

        request=requests.get(page_url, headers=headers)
        web_page=request.text
        soup=BeautifulSoup(web_page, "lxml")
        card_data=soup.find_all(class_="mediabox mediabox--linked")
        for i in card_data:
            card_title=i.get("title")
            card_img_url=i.a.source.get("srcset")
            card_id=i.a.get("data-design-id")
            card_url="https://99designs.com"+i.a.get("href")
            card_usr_profile="https://99designs.com"+i.div.div.span.span.next_sibling.a.get("href")
            card_usr_name=i.div.div.span.span.next_sibling.a.string
            card_usr_av=i.div.div.span.span.a.img.get("src")
            card_likes=i.div.div.next_sibling.div.span.string.strip()

            cards_data=[]
            cards_data.append(
                {
                    "Card_title": card_title,
                    "Card_ID": card_id,
                    "Card_image": card_img_url,
                    "Card_url": card_url,
                    "Card_user_profile": card_usr_profile,
                    "Card_user_name": card_usr_name,
                    "Card_user_avatar": card_usr_av,
                    "Card_likes": card_likes
                }
            )
            with open(f"Page_{page_num}.json", "a", encoding="utf-8") as file:
                json.dump(cards_data, file, indent=4, ensure_ascii=False)
            with open(f"Page_{page_num}.csv", "a", encoding="utf") as file:
                writer=csv.writer(file)
                writer.writerow(
                    (
                        card_title,
                        card_id,
                        card_img_url,
                        card_url,
                        card_usr_profile,
                        card_usr_name,
                        card_usr_av,
                        card_likes
                    )
                )
        page_num+=1

        status1=(f"Page # {page_num-1}: In process...")
        status2=("Status: Done.")
        print(status1)

        pages_quantity=pages_quantity-1
        if pages_quantity==0:
            print("Status: Done. Completed!")
            break
        sleep(random.randrange(1, 3))
        print(f"{status2} Pages remain: {pages_quantity}\n")
get_cards_data()
