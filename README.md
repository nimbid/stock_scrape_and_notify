# stock_scrape_and_notify
Scrape stock price data using Beautifulsoup and create desktop notifications.

The script uses BeautifulSoup4 to scrape stock prices from Moneycontrol and is compliant with its robots.txt
https://www.moneycontrol.com/robots.txt

There are 4 files here:
1. [input.py](https://github.com/nimbid/stock_scrape_and_notify/blob/master/input.py): Takes scrip name, Moneycontrol scrip page URL, buy price, stop loss, and target price, as input and creates a table in a csv file.
2. [stockscraper.py](https://github.com/nimbid/stock_scrape_and_notify/blob/master/stockscraper.py): Takes path of portfolio csv file as input. Checks if stop-loss or target price have been reached. Notifications show stop loss/target if they are reached, and show current price otherwise.
3. [stockscraper_windows.py](https://github.com/nimbid/stock_scrape_and_notify/blob/master/stockscraper_windows.py): Does the same as stockscraper.py but for Windows.
4. [scheduler_cron.txt](https://github.com/nimbid/stock_scrape_and_notify/blob/master/scheduler_cron.txt): Contains a sample cron job to use the script for monitoring the portfolio.

## Pre-requisites
* Python 3.x
* Libraries:
  - [win10toast](https://pypi.org/project/win10toast/)
  - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Instructions
1. Run input.py to create your portfolio file. You will need to pass a path as input where the script will create a file named 'portfolio.csv'.
2. Run stockscraper.py or stockscraper_windows.py (depending on your operating system). Pass the path of the portfolio file as input to this.

**Tips**:
* Run stockscraper.py/stockscraper_windows.py as part of a cron job (can use [scheduler_cron.txt](https://github.com/nimbid/stock_scrape_and_notify/blob/master/scheduler_cron.txt) as a reference) to use this script as a monitoring script.
* To change your portfolio, you can either run input.py again or modify the csv file directly.
