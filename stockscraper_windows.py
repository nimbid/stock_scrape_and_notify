# coding: utf-8
import os
import csv
import datetime
from time import sleep
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#Create Windows10 display notification.
def notify(title, text):
    toaster = ToastNotifier()
    toaster.show_toast(title, text)

#Get portfolio file path from user.
loc=input("Enter path of portfolio file: ")
print ("\n")  #Go to new line

#Added hard-coded value here for location as cron job won't run with dependency on user input.
#loc='/Users/bnimish/Desktop/portfolio.csv'

#Read portfolio table from saved csv file.
#First row of table will have titles. Start from 2nd row when making HTTP requests.
table = []
def readfromfile(location):
    with open(location, 'r') as portfolio:
        reader = csv.reader(portfolio)
        for row in reader:
            table.append(row)
    return table

#Check if stop-loss or target price have been reached. Notify if triggered and show current price otherwise.
def evaluate_conditions(stoplosscheck, targetpricecheck, cmp, stockname):
    #Convert values to float for evaluation.
    slcheck = float(stoplosscheck)
    tpcheck = float(targetpricecheck)
    p = float(cmp)
    if p <= slcheck:
        notify(stockname, "Stop Loss Triggered: " + cmp)
    elif p >= tpcheck:
        notify(stockname, "Target Price Reached: " + cmp)
    else:
        notify(stockname, "Current Price: " + cmp)

#Method will use input from portfolio table and scrape webpages.
def scraper(scrapingtable=readfromfile(loc)):
    tab = scrapingtable
    for item in tab[1:]:
        #specify the url
        quote_page = item[1]
        #quote_page = 'https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/lupin/L'
        # query the website and return the html to the variable ‘page’
        page = urlopen(Request(quote_page, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}))
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
        # Take out the <div> of name and get its value
        name_box = soup.find('h1', attrs={'class': 'pcstname'})
        name = name_box.text.strip() # strip() is used to remove starting and trailing
        #Print date and time, followed by scrip name and price.
        now = datetime.datetime.now()
        print ("Date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
        print (name)
        # get the index price
        price_box = soup.find('div', attrs={'class': 'pcnsb div_live_price_wrap'}).find_next('span')
        price = price_box.text
        #num_price=float(price)
        print (price)
        evaluate_conditions(item[3], item[4], price, name)
        sleep(5)

scraper(table)
print ("\n")#Add new line after execution
