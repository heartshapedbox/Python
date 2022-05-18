import os
os.chdir("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2")
import requests
import json
import csv
import re
import random
from random import randrange
from time import sleep
from bs4 import BeautifulSoup
from progress.bar import (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar, ShadyBar)
from progress.spinner import (Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner)
from progress.counter import Counter, Countdown, Stack, Pie
from progress.colors import bold


url = "https://www.calories.info/"
headers = {
    "access-control-allow-credentials": "true",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36"
}

request = requests.get(url, headers=headers)
web_page = request.text

with open("index.html", "w", encoding="utf-8") as file:
    file.write(web_page)

with open("C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\index.html", encoding="utf-8") as file:
    webpage_text = file.read()

soup = BeautifulSoup(webpage_text, "lxml")

# create main object for .json file
categories_info_object = {}

# get a list of categories with titles and links
categories_links = soup.find_all(class_="menu-item-object-calorietables")
def get_categories_links(n):
    list = [0 for i in n]
    for i in range(len(n)):
        category_name = n[i].string
        category_url = n[i].a.get("href")
        # put data in categories_info_object
        categories_info_object[category_name] = category_url
    return categories_info_object
get_categories_links(categories_links)

# create .json file
with open("categories_info_object.json", "w", encoding="utf-8") as file:
    json.dump(categories_info_object, file, indent=4, ensure_ascii=False)


with open("categories_info_object.json", encoding='utf-8') as file:
    all_categories = json.load(file)


#to count iterations
iterations_count = int(len(all_categories))
print(f"Total iterations: {iterations_count}")

# to count categories
count = 0

#bar progress
bar = IncrementalBar(bold('Progress'), color = 'green', max = iterations_count, suffix = "%(percent)d%% [%(index)d/%(max)d]")


# get data from each category (link)
for category_name, category_url in all_categories.items():

    #replace coma, space and dash with underscore
    rep = [",", " ", "-"]
    for i in rep:
        if i in category_name:
            category_name = category_name.replace(i, "_")
    #replace coma, space and dash with underscore

    req = requests.get(url=category_url, headers=headers)
    web_page = req.text

    with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\data\\{count}_{category_name}.html", "w", encoding="utf-8") as file:
        file.write(web_page)

    with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\data\\{count}_{category_name}.html", encoding="utf-8") as file:
        webpage_text = file.read()

    soup = BeautifulSoup(webpage_text, "lxml")

    # table header
    table_head = soup.find("thead").find("tr").find_all("td")
    product = table_head[0].string
    serving_100 = table_head[1].string
    calories_100 = table_head[4].string
    kilojoules_100 = table_head[5].string

    # create .csv file and put table header in it
    with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\data\\{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                serving_100,
                calories_100,
                kilojoules_100
            )
        )

    # get products data
    products_data = soup.find("body").find_all("tr", class_="kt-row")

    category_main_title = soup.find("h1", class_="page-title").string
    category_main_url = soup.find(class_="entry-content-thumbnail").img.get("src")
    category_main_description = soup.find("div", id="calories-desc-before-wrapper").find("p").string

    product_list = []

    category_descripton = []
    category_descripton.append(
        {
            "Category name": category_main_title,
            "Category url": category_main_url,
            "Category description": category_main_description,
        }
    )

    # create new .json file
    with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\data\\{count}_{category_name}.json", "w", encoding="utf-8") as file:
        json.dump(category_descripton, file, indent=4, ensure_ascii=False)


    for i in products_data:
        item_td = i.find_all("td")
        item_name = item_td[0].find("a").string
        item_serving_100 = item_td[1].find("data").string
        # extract redundant tag <data>
        extr_data_tag = item_td[1].data.extract()
        # get units
        item_serving_100_unit = item_td[1].string
        item_calories_100 = item_td[4].find("data").string + " cal"
        item_kilojoules_100 = item_td[5].find("data").string + " kj"

        product_list.append(
            {
                "Product title": item_name,
                "Serving": item_serving_100,
                "Serving unit": item_serving_100_unit,
                "Calories": item_calories_100,
                "Kilojoules": item_kilojoules_100
            }
        )

        # add product data to .csv file with "a" (append) flag instead of "w"
        with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\data\\{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    item_name,
                    item_serving_100 + " " + item_serving_100_unit,
                    item_calories_100,
                    item_kilojoules_100
                )
            )

    # update .json file
    with open(f"C:\\Users\\baben\\Documents\\GitHub\\python\\scraping\\lesson2\\data\\{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_list, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"Iteration #: {count}. {category_name}")
    iterations_count -= 1

    if iterations_count != 0:
        bar.next()
        print(f"  Iterations remain: {iterations_count}")
        sleep(random.randrange(1, 2))
    else:
        bar.next()
        print("  Complete.")
        break
        bar.finish()
