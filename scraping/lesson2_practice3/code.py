import os
os.chdir ("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\data")
import re
import requests
import json
import csv
import random
from random import randrange
from time import sleep
from bs4 import BeautifulSoup

url="https://www.kobo.com/ww/en/ebooks/categories"
headers={
    "Access-Control-Allow-Credentials": "true",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36"
}

def get_parent_categories():
    request=requests.get(url, headers=headers)
    webpage=request.text

    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\index.html", "w", encoding="utf-8") as file:
        file.write(webpage)
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\index.html", encoding="utf-8") as file:
        webpage_text=file.read()

    soup=BeautifulSoup(webpage_text, "lxml")
    parent_categories={}
    parent_cat=soup.find_all("div", class_="category-facet-item-container gizmo-collapsible-with-header only-in-small")

    for i in parent_cat:
        parent_cat_name=i.h2.a.string
        parent_cat_url="https://www.kobo.com"+i.h2.a.get("href")
        rep=[", ", " ", "/", ".", ":", "'", "-"]
        for x in rep:
            if x in parent_cat_name:
                parent_cat_name=parent_cat_name.replace(x,"_")
        parent_categories[parent_cat_name]=parent_cat_url

    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\parent_categories\\parent_categories.json", "w", encoding="utf-8") as file:
        json.dump(parent_categories, file, indent=4, ensure_ascii=False)
get_parent_categories()

def get_sub_categories():
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\parent_categories\\parent_categories.json", encoding="utf-8") as file:
        par_cat=json.load(file)

    count=1
    sub_categories={}
    for parent_cat_name, parent_cat_url in par_cat.items():
        if parent_cat_name=="Periodicals":
            continue
        request=requests.get(url=parent_cat_url, headers=headers)
        webpage=request.text
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\parent_categories]\{count}_{parent_cat_name}.html", "w", encoding="utf-8") as file:
            file.write(webpage)
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\parent_categories\\{count}_{parent_cat_name}.html", encoding="utf-8") as file:
            webpage_text=file.read()
        soup=BeautifulSoup(webpage_text, "lxml")
        sub_cat=soup.find(class_="single-select facet-list scrollable list").find_all("li")
        for i in sub_cat:
            sub_cat_name=i.a.string
            sub_cat_url="https://www.kobo.com"+i.a.get("href")
            rep=[", ", " ", "/", ".", ":", "'", "-", "?"]
            for x in rep:
                if x in sub_cat_name:
                    sub_cat_name=sub_cat_name.replace(x,"_")
            sub_categories[sub_cat_name]=sub_cat_url
        count+=1
        with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\sub_categories\\sub_categories.json", "w", encoding="utf-8") as file:
            json.dump(sub_categories, file, indent=4, ensure_ascii=False)
get_sub_categories()

def get_all_pages_of_sub_categories():
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\sub_categories\\sub_categories.json", encoding="utf-8") as file:
        sb_cat=json.load(file)

    sub_categories_pages={}
    sub_cat_page_num=1
    for sub_cat_name, sub_cat_url in sb_cat.items():
        request=requests.get(sub_cat_url, headers=headers)
        webpage=request.text
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\sub_categories\\{sub_cat_page_num}_{sub_cat_name}.html", "w", encoding="utf-8") as file:
            file.write(webpage)
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\sub_categories\\{sub_cat_page_num}_{sub_cat_name}.html", encoding="utf-8") as file:
            webpage_text=file.read()
        soup=BeautifulSoup(webpage_text, "lxml")
        for i in range(1,100):
            page_url="https://www.kobo.com"+soup.find(class_="page-link first active").get("href")
            if "=1" in page_url:
                page_url=page_url.replace("=1","="+str(i))
                page_name=f"{sub_cat_name}_{i}"
                sub_categories_pages[page_name]=page_url
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\sub_categories\\sub_categories_pages.json", "w", encoding="utf-8") as file:
            json.dump(sub_categories_pages, file, indent=4, ensure_ascii=False)
        sub_cat_page_num+=1
get_all_pages_of_sub_categories()

def get_books_data():
    with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice3\\sub_categories\\sub_categories_pages.json", encoding="utf-8") as file:
        sb_cat_pages=json.load(file)

    total_pages=int(len(sb_cat_pages))
    print(f"Total pages: {total_pages}\n")

    page_count=1
    for page_name, page_url in sb_cat_pages.items():
        request=requests.get(url=page_url, headers=headers)
        webpage=request.text
        with open(f"{page_count}_{page_name}.html", "w", encoding="utf-8") as file:
            file.write(webpage)
        with open(f"{page_count}_{page_name}.html", encoding="utf-8") as file:
            webpage_text=file.read()
        with open(f"{page_count}_{page_name}.csv", "w", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(
                (
                    "Book name",
                    "Book headline",
                    "Book contributor",
                    "Book series",
                    "Book cover",
                    "Book page",
                    "Book language",
                    "Book publish date",
                    "Book format",
                    "Book ISBN",
                    "Book description",
                    "Book rating",
                    "Book price"
                )
            )

        soup=BeautifulSoup(webpage_text, "lxml")
        book_data=soup.find_all(class_="item-detail")

        for i in book_data:
            book_title=i.script.string
            book_title=book_title.split('name": "')[-1]
            book_title=book_title.split('"')[0]
            if "\\u0027s" in book_title:
                book_title=book_title.replace("\\u0027s","'s")
            if "\\u0027" in book_title:
                book_title=book_title.replace("\\u0027","")
            if "\\u0026" in book_title:
                book_title=book_title.replace("\\u0026","and")
            if "\\u0022" in book_title:
                book_title=book_title.replace("\\u0022", "'")

            book_alt_headline=i.script.string
            book_alt_headline=book_alt_headline.split('alternativeHeadline": "')[-1]
            book_alt_headline=book_alt_headline.split('"')[0].strip()
            if "{" in book_alt_headline:
                book_alt_headline=book_alt_headline.replace("{", "none")
            if "\\u0027s" in book_alt_headline:
                book_alt_headline=book_alt_headline.replace("\\u0027s","'s")
            if "\\u0027" in book_alt_headline:
                book_alt_headline=book_alt_headline.replace("\\u0027","")
            if "\\u0026" in book_alt_headline:
                book_alt_headline=book_alt_headline.replace("\\u0026","and")
            if "\\u0022" in book_alt_headline:
                book_alt_headline=book_alt_headline.replace("\\u0022", "'")
            if book_alt_headline=="none":
                book_alt_headline=None

            try:
                book_contr=i.div.next_sibling.next_sibling.div.div.span.next_sibling.next_sibling.a.string
            except AttributeError:
                book_contr=None

            try:
                book_series=i.div.next_sibling.next_sibling.div.next_sibling.next_sibling.span.next_sibling.next_sibling.a.string
            except AttributeError:
                book_series=None

            book_cover=i.script.string
            book_cover=book_cover.split('thumbnailUrl": "')[-1]
            book_cover=book_cover.split('"')[0]
            rep=["180", "30", "215"]
            for r in rep:
                if r in book_cover:
                    book_cover=book_cover.replace(r, "1000")

            book_ref=i.script.string
            book_ref=book_ref.split('"url": "')[-1]
            book_ref=book_ref.split('"')[0]

            book_lan=i.script.string
            book_lan=book_lan.split('inLanguage": "')[-1]
            book_lan=book_lan.split('"')[0]

            book_pub_data=i.script.string
            book_pub_data=book_pub_data.split('datePublished": "')[-1]
            book_pub_data=book_pub_data.split('"')[0]
            if "{" in book_pub_data:
                book_pub_data=book_pub_data.replace("{", "none")

            book_format=i.script.string
            book_format=book_format.split('bookFormat": "')[-1]
            book_format=book_format.split('"')[0]
            if "{" in book_format:
                book_format=book_format.replace("{", "none")

            book_isbn=i.script.string
            book_isbn=book_isbn.split('isbn": "')[-1]
            book_isbn=book_isbn.split('"')[0]
            if "{" in book_isbn:
                book_isbn=book_isbn.replace("{", "none")

            book_plot=i.script.string
            book_plot=book_plot.split('description": "')[-1]
            book_plot=book_plot.split('"')[0]
            book_plot=book_plot+"..."
            if "{" in book_plot:
                book_plot=book_plot.replace("{", "none")
            if "\\u0027s" in book_plot:
                book_plot=book_plot.replace("\\u0027s","'s")
            if "\\u0027" in book_plot:
                book_plot=book_plot.replace("\\u0027","")
            if "\\u0026" in book_plot:
                book_plot=book_plot.replace("\\u0026","and")
            if "\\u0022" in book_plot:
                book_plot=book_plot.replace("\\u0022", "'")
            if "......" in book_plot:
                book_plot=book_plot.replace("......", "...")

            book_rating=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get("aria-label")
            if book_rating==None:
                try:
                    book_rating=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get("aria-label")
                except:
                    book_rating=None

            if book_rating==None:
                try:
                    book_rating=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get("aria-label")
                except:
                    book_rating=None

            try:
                book_price=i.div.next_sibling.next_sibling.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.span.span.string.strip()
            except AttributeError:
                try:
                    book_price=i.div.next_sibling.next_sibling.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.span.span.string.strip()
                except AttributeError:
                    try:
                        book_price=i.div.next_sibling.next_sibling.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.span.span.string.strip()
                    except AttributeError:
                        try:
                            book_price=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.span.span.string.strip()
                        except AttributeError:
                            try:
                                book_price=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.span.span.string.strip()
                            except AttributeError:
                                try:
                                    book_price=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.span.span.string.strip()
                                except AttributeError:
                                    book_price="alt_price"
            try:
                book_price_alt=i.div.next_sibling.next_sibling.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.next_sibling.next_sibling.span.span.string.strip()
            except AttributeError:
                try:
                    book_price_alt=i.div.next_sibling.next_sibling.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.next_sibling.next_sibling.span.span.string.strip()
                except AttributeError:
                    try:
                        book_price_alt=i.div.next_sibling.next_sibling.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.next_sibling.next_sibling.span.span.string.strip()
                    except AttributeError:
                        try:
                            book_price_alt=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.next_sibling.next_sibling.span.span.string.strip()
                        except AttributeError:
                            try:
                                book_price_alt=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.next_sibling.next_sibling.span.span.string.strip()
                            except AttributeError:
                                try:
                                    book_price_alt=i.div.next_sibling.next_sibling.h2.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.span.next_sibling.next_sibling.span.span.string.strip()
                                except AttributeError:
                                    book_price_alt=None

            if "alt_price" in book_price:
                book_price=book_price_alt
            if book_price==None:
                book_price="Free"

            book_data_obj=[]
            book_data_obj.append(
                {
                    "Book name": book_title,
                    "Book headline": book_alt_headline,
                    "Book contributor": book_contr,
                    "Book series": book_series,
                    "Book cover": book_cover,
                    "Book page": book_ref,
                    "Book language": book_lan,
                    "Book publish date": book_pub_data,
                    "Book format": book_format,
                    "Book ISBN": book_isbn,
                    "Book description": book_plot,
                    "Book rating": book_rating,
                    "Book price": book_price
                }
            )

            with open(f"{page_count}_{page_name}.json", "a", encoding="utf-8") as file:
                json.dump(book_data_obj, file, indent=4, ensure_ascii=False)
            with open(f"{page_count}_{page_name}.csv", "a", encoding="utf-8") as file:
                writer=csv.writer(file)
                writer.writerow(
                    (
                        book_title,
                        book_alt_headline,
                        book_contr,
                        book_series,
                        book_cover,
                        book_ref,
                        book_lan,
                        book_pub_data,
                        book_format,
                        book_isbn,
                        book_plot,
                        book_rating,
                        book_price
                    )
                )

        page_count+=1
        status1=(f"Page #{page_count-1} {page_name}: In process...")
        status2=("Status: Done.")
        print(status1)

        total_pages=total_pages-1
        if total_pages==0:
            print("Status: Done. All pages processed!")
            break
        sleep(random.randrange(1, 3))
        print(f"{status2} Pages remain: {total_pages}\n")
get_books_data()
