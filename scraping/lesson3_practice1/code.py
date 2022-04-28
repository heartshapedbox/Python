import os
os.chdir("D:\Code\Python\Scraping\lesson3_practice1\data")
import re
import requests
import csv
import xlsxwriter
import json
import pandas
import random
from random import randrange
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

url="https://zoon.com.ua/kiev/beauty/"

def get_all_cards_urls_on_page(url):
    driver=webdriver.Chrome(
        executable_path="D:\Code\Python\Scraping\lesson3_practice1\chromedriver\chromedriver"
    )
    driver.maximize_window()

    try:
        driver.get(url=url)
        while True:
            element_to_get_more_urls=driver.find_element_by_class_name("catalog-button-showMore")
            if element_to_get_more_urls.is_displayed()==False:
                with open("D:\Code\Python\Scraping\lesson3_practice1\index.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                break
            else:
                actions=ActionChains(driver)
                actions.move_to_element(element_to_get_more_urls).perform()
                sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_cards_urls():
    with open("D:\Code\Python\Scraping\lesson3_practice1\index.html", encoding="utf-8") as file:
        webpage_text=file.read()
    soup=BeautifulSoup(webpage_text, "lxml")
    get_card_url=soup.find_all(class_="minicard-item__title")
    cards_urls={}
    card_num=0
    for i in get_card_url:
        card_url=i.a.get("href")
        card_name=i.a.get("href").split("/")[-2].capitalize()
        card_num+=1
        cards_urls[card_name]=card_url
        with open("D:\Code\Python\Scraping\lesson3_practice1\cards_urls.json", "w", encoding="utf-8") as file:
            json.dump(cards_urls, file, indent=4, ensure_ascii=False)

def get_cards_data():
    with open("D:\Code\Python\Scraping\lesson3_practice1\cards_urls.json", encoding="utf-8") as file:
        card_urls=json.load(file)

        total_cards=int(len(card_urls))
        print(f"Total cards: {total_cards}")

        card_count=1
        for card_name, card_url in card_urls.items():
            request=requests.get(card_url)
            webpage=request.text
            with open(f"{card_count}_{card_name}.html", "w", encoding="utf-8") as file:
                file.write(webpage)
            with open(f"{card_count}_{card_name}.html", encoding="utf-8") as file:
                webpage_text=file.read()
            soup=BeautifulSoup(webpage_text, "lxml")


            card_title=soup.find(class_="service-page-header").find("h1").find("span").string


            try:
                find_card_images_urls=soup.find(class_="gallery-controls").find("ul").find_all("li")
                card_gallery_urls_list=[]
                for i in find_card_images_urls:
                    card_gallery_urls_list.append(i.a.get("href"))
            except AttributeError:
                find_card_images_urls=None
            card_gallery_urls=", ".join(str(i) for i in card_gallery_urls_list)


            try:
                card_main_image_url=card_gallery_urls_list[0]
            except AttributeError:
                card_main_image_url=None


            find_card_description=soup.find(class_="js-desc oh word-break").find_all("p")
            description_list=[]
            for i in find_card_description:
                card_description=i.text.strip()
                if card_description=="":
                    continue
                description_list.append(card_description)
            card_description_text=" ".join(str(i) for i in description_list)
            if "\n" in card_description_text:
                card_description_text=card_description_text.replace("\n"," ")


            find_card_details_name=soup.find(class_="service-description-block").find_all("dt")
            find_card_details_description=soup.find(class_="service-description-block").find_all("dd")
            card_details_list=[]
            try:
                card_details_title=find_card_details_name[0].string.strip()+":"
                card_details_list.append(card_details_title)
                card_details_description=find_card_details_description[0].text
                card_details_list.append(card_details_description)
            except IndexError:
                card_details_title=None
                card_details_description=None
            try:
                card_details_title1=find_card_details_name[1].string.strip()+":"
                card_details_list.append(card_details_title1)
                card_details_description1=find_card_details_description[1].text
                card_details_list.append(card_details_description1)
            except IndexError:
                card_details_title1=None
                card_details_description1=None
            try:
                card_details_title2=find_card_details_name[2].string.strip()+":"
                card_details_list.append(card_details_title2)
                card_details_description2=find_card_details_description[2].text+"."
                card_details_list.append(card_details_description2)
            except IndexError:
                card_details_title2=None
                card_details_description2=None
            card_details=". ".join(str(i).strip() for i in card_details_list)
            if ":." in card_details:
                card_details=card_details.replace(":.",":")


            card_summary=card_description_text+" "+card_details


            card_working_hours_list=[]
            try:
                find_card_working_hours=soup.find(class_="fluid uit-cover").find("dd").find("div").next_element.strip()
                card_working_hours_list.append(find_card_working_hours)
            except TypeError:
                try:
                    find_card_working_hours=soup.find(class_="fluid uit-cover").find("dd").find("div").a.string.strip()
                    card_working_hours_list.append(find_card_working_hours)
                except AttributeError:
                    find_card_working_hours=None
            except AttributeError:
                find_card_working_hours=None
            try:
                find_card_working_hours_extra_info=soup.find(class_="fluid uit-cover").find("dd").find("div").find("br").next_element.strip()
                card_working_hours_list.append(find_card_working_hours_extra_info)
            except AttributeError:
                find_card_working_hours_extra_info=None
            card_working_hours=", ".join(str(i) for i in card_working_hours_list)


            try:
                find_card_phones=soup.find(class_="service-phones-list").find_all(class_="tel-phone js-phone-number")
                card_phones_list=[]
                for i in find_card_phones:
                    card_phone=i.get("href")
                    if "tel:" in card_phone:
                        card_phone=card_phone.replace("tel:","")
                    card_phones_list.append(card_phone)
            except AttributeError:
                find_card_phones=None
            card_phones=", ".join(str(i) for i in card_phones_list)


            card_address_list=[]
            card_address_details1=soup.find(class_="iblock").text.strip()
            card_address_list.append(card_address_details1)
            try:
                card_address_details2=soup.find(class_="iblock").next_sibling.next_sibling.text.strip()
                card_address_list.append(card_address_details2)
            except AttributeError:
                card_address_details2=""
            try:
                card_address_details3="Станция м."+soup.find(class_="address-metro invisible-links").a.text.strip()
                card_address_list.append(card_address_details3)
            except AttributeError:
                card_address_details3=""
            card_address=", ".join(str(i) for i in card_address_list)


            card_websites_list=[]
            try:
                find_card_website=soup.find_all(class_="service-website")
                for i in find_card_website:
                    find_card_website_urls=i.find_all("a")
                    for e in find_card_website_urls:
                        card_website=e.get("href")
                        if "to=" in card_website:
                            card_website=card_website.split("=")[1]
                        if "to=" in card_website:
                            card_website=card_website.split("=")[1]
                        if "/?token" in card_website:
                            card_website=card_website.split("/?token")[0]
                        if "&hash" in card_website:
                            card_website=card_website.split("&hash")[0]
                        if "%3A%2F%2F" in card_website:
                            card_website=card_website.replace("%3A%2F%2F","://")
                        if "%2F&" in card_website:
                            card_website=card_website.replace("%2F&","/")
                        if "%2F" in card_website:
                            card_website=card_website.replace("%2F","/")
                        if "www." in card_website:
                            card_website=card_website.replace("www.","")
                        card_websites_list.append(card_website)
                card_websites=", ".join(str(i) for i in card_websites_list)
            except AttributeError:
                find_card_website=None


            data_container=[]
            data_container.append(
                {
                    "Card_title": card_title,
                    "Card_url": card_url,
                    "Card_main_image": card_main_image_url,
                    "Card_gallery": card_gallery_urls,
                    "Card_description": card_summary,
                    "Card_working_hours": card_working_hours,
                    "Card_phone_numbers": card_phones,
                    "Card_address": card_address,
                    "Card_website": card_websites
                }
            )

            with open(f"{card_count}_{card_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_container, file, indent=4, ensure_ascii=False)

            #create .xlsx file and put data inside
            workbook=xlsxwriter.Workbook(f"{card_count}_{card_name}.xlsx", {'strings_to_urls': False})
            worksheet=workbook.add_worksheet()
            data=(
                ["Card_title", card_title],
                ["Card_url", card_url],
                ["Card_main_image", card_main_image_url],
                ["Card_gallery", card_gallery_urls],
                ["Card_description", card_summary],
                ["Card_working_hours", card_working_hours],
                ["Card_phone_numbers", card_phones],
                ["Card_address", card_address],
                ["Card_website", card_websites]
            )
            column,row=0,0
            for title, element in (data):
                worksheet.write(column, row, title)
                worksheet.write(column+1, row, element)
                row+=1
            workbook.close()

            card_count+=1
            status1=(f"Card #{card_count-1} {card_name}: In process...")
            status2=("Status: Done.")
            print(status1)

            total_cards-=1
            if total_cards==0:
                print("Status: Done. All cards processed!")
                break
            sleep(random.randrange(1, 3))
            print(f"{status2} Cards remain: {total_cards}\n")

def get_data():
    get_all_cards_urls_on_page(url)
    get_cards_urls()
    get_cards_data()
get_data()
