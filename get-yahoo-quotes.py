#!/usr/bin/env python

"""
get-yahoo-quotes.py:  Script to download Yahoo historical quotes using the new cookie authenticated site.
 Usage: get-yahoo-quotes SYMBOL (optional)START_DATE (optional)END_DATE
 History
 06-03-2017 : Created script
"""

__author__ = "Brad Luicas"
__copyright__ = "Copyright 2017, Brad Lucas"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Brad Lucas"
__email__ = "brad@beaconhill.com"
__status__ = "Production"


import re
import sys
import time
import requests
import calendar


from epoch_time_retrieval import get_today_epoch, get_time_epoch


def split_crumb_store(v):
    return v.split(':')[2].strip('"')


def find_crumb_store(lines):
    # Looking for
    # ,"CrumbStore":{"crumb":"9q.A4D1c.b9
    for l in lines:
        if re.findall(r'CrumbStore', l):
            return l
    print("Did not find CrumbStore")


def get_cookie_value(r):
    return {'B': r.cookies['B']}


def get_page_data(symbol):
    url = "https://finance.yahoo.com/quote/%s/?p=%s" % (symbol, symbol)
    r = requests.get(url)
    cookie = get_cookie_value(r)

    # Code to replace possible \u002F value
    # ,"CrumbStore":{"crumb":"FWP\u002F5EFll3U"
    # FWP\u002F5EFll3U
    lines = r.content.decode('unicode-escape').strip(). replace('}', '\n')
    return cookie, lines.split('\n')


def get_cookie_crumb(symbol):
    cookie, lines = get_page_data(symbol)
    crumb = split_crumb_store(find_crumb_store(lines))
    return cookie, crumb


def get_data_as_csv(symbol, start_date, end_date, cookie, crumb):
    url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&crumb=%s" % (symbol, start_date, end_date, crumb)
    response = requests.get(url, cookies=cookie)
    content_data = response.content.decode('utf-8')
    csv_data = content_data.split('\n')
    
    return csv_data
    

def download_quotes_as_csv(symbol, start_date, end_date):
    cookie, crumb = get_cookie_crumb(symbol)
    csv_data = get_data_as_csv(symbol, start_date, end_date, cookie, crumb)
    
    return csv_data


def write_data_to_file(filename, content_data_lines):
    with open (filename, 'w') as handle:
        for line in content_data_lines:
            handle.write(line + '\n')


def main():
    start_date = get_time_epoch('1970-01-01')
    end_date = get_today_epoch()

    if len(sys.argv) == 1:
        print("\nUsage: get-yahoo-quotes.py SYMBOL [optional yyyy-mm-dd]START_DATE [optional yyyy-mm-dd]END_DATE\n\n")
        return
    
    symbol = sys.argv[1]    
    if len(sys.argv) > 2:
        start_date = get_time_epoch(sys.argv[2])
    
    if len(sys.argv) > 3:
        end_date = get_time_epoch(sys.argv[3])
    
    print("Downloading %s to %s.csv" % (symbol, symbol))
    
    csv_data = download_quotes_as_csv(symbol, start_date, end_date)
    filename = '%s.csv' % (symbol)
    write_data_to_file(filename, csv_data)


if __name__ == '__main__':
    print("--------------------------------------------------")
    main()
