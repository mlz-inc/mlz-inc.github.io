#!/usr/bin/env python3
from bs4 import BeautifulSoup
from datetime import datetime
import requests as req
import re

AMOUNT_DAYS = 30
PAGES = 5

def last_act(tag):
    return tag.text == "Последнее посещение:"

def check_activity(acmp, link):
    resp = req.get(acmp + link)
    resp.encoding = 'cp1251'
    
    soup = BeautifulSoup(resp.text, 'lxml')
    needed = soup.find(last_act)
    needed = needed.next_sibling.next_sibling
    
    date = needed.text
    day, month, year, *oth = date.split()


    months = {'января' : 1,
              'февраля' : 2,
              'марта' : 3,
              'апреля' : 4,
              'мая' : 5,
              'июня' : 6,
              'июля' : 7,
              'августа' : 8,
              'сентября' : 9,
              'октября' : 10,
              'ноября' : 11,
              'декабря' : 12}
    year = int(year)
    month = int(months[month])
    day = int(day)
    
    now = datetime.now()
    #then = datetime(2017, 2, 26)
    then = datetime(year, month, day)
    delta = now - then
    days = delta.days
    
    return days < AMOUNT_DAYS

def main():    
    acmp = "https://acmp.ru"
    top_meleuz = "/index.asp?main=rating&str=%EC%E5%EB%E5%F3%E7&page="
    # получение рейтинга по запросу мелеуз на acmp.ru

    number = 0
    for page in range(0, PAGES):
        page_link = acmp + top_meleuz + str(page)
        resp = req.get(page_link) 
        resp.encoding = 'cp1251' # чтобы работал русский язык

        soup = BeautifulSoup(resp.text, 'lxml') # resp.text for req

        right = soup.find("table", cellspacing="1") # единственный ориентир
        
        for elem in right.children:
            if elem.name and elem.td:
                name = elem.td.next_sibling.next_sibling
                link = name.a
                if check_activity(acmp, link["href"]):
                    number += 1
                    place = name.next_sibling.next_sibling
                    tasks = place.next_sibling.next_sibling
                    score = tasks.next_sibling.next_sibling
                    print ('', number, name.text, place.text, tasks.text, score.text, '', sep = ' | ')

        # элемент tr для разбора
        #print(right.tr.next_sibling.next_sibling)

if __name__ == "__main__":
    main()
