# stock_scrape_and_notify
Scrape stock price data using Beautifulsoup and create desktop notifications.

The script uses BeautifulSoup4 to scrape stock prices from Moneycontrol and is compliant with its robots.txt
https://www.moneycontrol.com/robots.txt

There are 3 scripts here:
1. [input.py](https://github.com/nimbid/stock_scrape_and_notify/blob/master/input.py): Takes scrip name, Moneycontrol scrip page URL, buy price, stop loss, and target price, as input and creates a table in a CSV file.
2. [stockscraper.py](https://github.com/nimbid/stock_scrape_and_notify/blob/master/stockscraper.py): Takes path of portfolio CSV file as input. Checks if stop-loss or target price have been reached. Notifications show stop loss/target if they are reached, and show current price otherwise.
3. [stockscraper_windows.py](https://github.com/nimbid/stock_scrape_and_notify/blob/master/stockscraper_windows.py): Does the same as stockscraper.py but for Windows.

## Pre-requisites
* Python 3.x
* Libraries:
  - [win10toast](https://pypi.org/project/win10toast/)
  - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
