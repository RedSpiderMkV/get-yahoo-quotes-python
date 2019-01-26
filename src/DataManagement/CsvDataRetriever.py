#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:07:47 2019

@author: nikeah
"""

import requests
from Utils.CookieCrumbRetriever import CookieCrumbRetriever


class CsvDataRetriever:
    def __init__(self):
        self._cookie_crumb_retriever = CookieCrumbRetriever()
    

    def GetQuotes(self, symbol, start_date, end_date):
        cookie, crumb = self._cookie_crumb_retriever.GetCookieCrumb(symbol)
        csv_data = self._getCsvData(symbol, start_date, end_date, cookie, crumb)
        
        return csv_data
    
    
    def _getCsvData(self, symbol, start_date, end_date, cookie, crumb):
        url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&crumb=%s" % (symbol, start_date, end_date, crumb)
        response = requests.get(url, cookies=cookie)
        content_data = response.content.decode('utf-8')
        csv_data = content_data.split('\n')
        
        return csv_data