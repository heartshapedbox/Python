import os
os.chdir("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2_practice2\\data")
import re
import requests
import json
import csv
import random
from random import randrange
from time import sleep
from bs4 import BeautifulSoup

url="https://www.calories.info/"
headers={
    "access-control-allow-credentials": "true",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36"
}

request=requests.get(url, headers=headers)
web_page=request.text

with open("index_main.html", "w", encoding="utf-8") as file:
    file.write(web_page)

with open("index_main.html", encoding="utf-8") as file:
    web_page_text=file.read()
soup=BeautifulSoup(web_page_text, "lxml")


# get product categories' name and links
product_categories_list={}
product_category_name_and_url=soup.find("div", class_="menu-calorie-tables-container").find_all("a")

for i in product_category_name_and_url:
    product_category_name=i.string
    product_category_url=i.get("href")
    # replace space, coma and dash wiht underscore
    rep=[" ","-",", "]
    for i in rep:
        if i in product_category_name:
            product_category_name=product_category_name.replace(i, "_")
    product_categories_list[f"{product_category_name}"]=product_category_url

# create .json file with product categories' names and links inside
with open("product_categories_list.json", "w", encoding="utf-8") as file:
    json.dump(product_categories_list, file, indent=4, ensure_ascii=False)

# load .json file for further actions
with open("product_categories_list.json", encoding="utf-8") as file:
    prod_cat_list=json.load(file)


# add counter
counter=int(len(prod_cat_list))
print(f"Total iterations: {counter}")

count=0
# open each category
for product_category_name, product_category_url in prod_cat_list.items():
    request=requests.get(url=product_category_url, headers=headers)
    web_page=request.text

    with open(f"{count}_{product_category_name}.html", "w", encoding="utf-8") as file:
        file.write(web_page)
    with open(f"{count}_{product_category_name}.html", encoding="utf-8") as file:
        web_page_text=file.read()
    soup=BeautifulSoup(web_page_text, "lxml")

    # get product_category title, image url and description
    product_category_data=[]
    product_category_title=soup.find("h1", class_="page-title").string
    product_category_image_url=soup.find("div", class_="entry-content").find("img").get("src")
    product_category_description=soup.find("div", id="calories-desc-before-wrapper").p.string

    product_category_data.append(
        {
            "Category_title": product_category_title,
            "Category_image": product_category_image_url,
            "Category_description": product_category_description
        }
    )

    with open(f"{count}_{product_category_name}.json", "w", encoding="utf-8") as file:
        json.dump(product_category_data, file, indent=4, ensure_ascii=False)

    # get table headers
    table_header=soup.find("thead").find("tr").find_all("td")
    table_header_order="Order number"
    table_header_name=table_header[0].string
    table_header_serving=table_header[1].string
    table_header_calouries=table_header[4].string
    table_header_kilojoules=table_header[5].string

    # push table header into .csv file
    # create .csv fiel
    with open(f"{count}_{product_category_name}.csv", "w", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(
            (
                table_header_name,
                table_header_serving,
                table_header_calouries,
                table_header_kilojoules
            )
        )

    # get product data: name, serving and calories
    product_data=[]
    product_info=soup.find_all(class_="kt-row")

    for i in product_info:
        # get product name
        product_name=i.a.string
        # get product serving
        product_serving100=i.find(class_="serving 100g").data.string
        # det unit for serving
        extr_tag_data=i.find(class_="serving 100g").data.extract()
        product_serving100_unit=i.find(class_="serving").string

        # get product calories
        product_calories=i.find(class_="kcal").data.string
        # get unit for calories
        extr_tag_data_calories=i.find(class_="kcal").data.extract()
        product_calories_unit=i.find(class_="kcal").string

        # get product kilojoules
        product_kilojoules=i.find(class_="kj").data.string
        # get unit for kilojoules
        extr_tag_data_kilojoules=i.find(class_="kj").data.extract()
        product_kilojoules_unit=i.find(class_="kj").string

        # updated .csv file with "a" flag
        with open(f"{count}_{product_category_name}.csv", "a", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(
                (
                    product_name,
                    product_serving100 + " " + product_serving100_unit,
                    product_calories + product_calories_unit,
                    product_kilojoules + product_kilojoules_unit
                )
            )

        # push the data to product_data
        product_data.append(
            {
                "Product": product_name,
                "Serving": product_serving100 + " " + product_serving100_unit,
                "Calories": product_calories + product_calories_unit,
                "Kilojoules": product_kilojoules + product_kilojoules_unit
            }
        )

    # updated .json file with "a" flag
    with open(f"{count}_{product_category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_data, file, indent=4, ensure_ascii=False)

    count+=1
    print(f"Iteration: {count}. {product_category_name}")
    counter-=1
    if counter==0:
        print("Complete!")
        break
    print(f"Iterations remain: {counter}")
    sleep(random.randrange(2, 5))
