import os
import csv
import datetime
from time import sleep
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re


def notify(title, subtitle, text):
    """
    Create Macbook display notification.
    """
    os.system("""
              osascript -e 'display notification "{}" subtitle "{}" with title "{}" sound name "Glass"'
              """.format(text, subtitle, title))


def readfromfile(location):
    """
    Read portfolio table from saved csv file.
    First row of table will have titles. Start from 2nd row when making HTTP requests.
    """
    table=[]
    with open (location,'r') as portfolio:
        reader=csv.reader(portfolio)
        for row in reader:
            table.append(row)
    return table


def evaluate_conditions(stoplosscheck, targetpricecheck, cmp, stockname):
    """
    Check if stop-loss or target price have been reached. Notify if triggered and show current price otherwise.
    """
    #Convert values to float for evaluation.
    slcheck=float(stoplosscheck)
    tpcheck=float(targetpricecheck)
    cmp_float_str=re.sub('[^0-9.]', '', cmp)  # Strip everything but numbers and period.
    p=float(cmp_float_str)
    if p<=slcheck:
        notify(stockname,"Stop Loss Triggered",cmp_float_str)
    elif p>=tpcheck:
        notify(stockname,"Target Price Reached",cmp_float_str)
    else:
        notify(stockname,"Current Price",cmp_float_str)


def scraper(tab):
    """
    Method will use input from portfolio table and scrape webpages.
    """
    for item in tab[1:]:
        # specify the url
        quote_page = item[1]
        #quote_page = 'https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/lupin/L'
        # query the website and return the html to the variable ‘page’
        page = urlopen(Request(quote_page,headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'Pragma':'no-cache'}))
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
        # Take out the <div> of name and get its value
        name_box = soup.find('div', attrs={'class': 'inid_name'}).find_next('h1')
        name = name_box.text.strip() # strip() is used to remove starting and trailing
        #Print date and time, followed by scrip name and price.
        now = datetime.datetime.now()
        print ("Date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
        print (name)
        # get the index price
        price_box = soup.find('div', attrs={'class':'inprice1 nsecp'})
        # print(price_box)
        price = price_box.text
        print(price)
        evaluate_conditions(item[3], item[4], price, name)
        sleep(5)


def main():
    """
    Entry point
    """
    #Get portfolio file path from user.
    loc=input("Enter path of portfolio file: ")
    print ("\n")  #Go to new line
    #Added hard-coded value here for location as cron job won't run with dependency on user input.
    #loc='/Users/username/path/portfolio.csv'
    scraper(readfromfile(loc))
    print ("\n")  #Add new line after execution


if __name__ == "__main__":
    main()
