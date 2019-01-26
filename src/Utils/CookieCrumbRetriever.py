#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:58:02 2019

@author: nikeah
"""

import re
import requests


class CookieCrumbRetriever:
    
    def GetCookieCrumb(self, symbol):
        cookie, lines = self._get_page_data(symbol)
        crumb = self._split_crumb_store(self._find_crumb_store(lines))
        return cookie, crumb
    
        
    def _split_crumb_store(self, v):
        return v.split(':')[2].strip('"')
    
    
    def _find_crumb_store(self, lines):
        # Looking for
        # ,"CrumbStore":{"crumb":"9q.A4D1c.b9
        for l in lines:
            if re.findall(r'CrumbStore', l):
                return l
        print("Did not find CrumbStore")
    
    
    def _get_cookie_value(self, r):
        return {'B': r.cookies['B']}
    
    
    def _get_page_data(self, symbol):
        url = "https://finance.yahoo.com/quote/%s/?p=%s" % (symbol, symbol)
        r = requests.get(url)
        cookie = self._get_cookie_value(r)
    
        # Code to replace possible \u002F value
        # ,"CrumbStore":{"crumb":"FWP\u002F5EFll3U"
        # FWP\u002F5EFll3U
        lines = r.content.decode('unicode-escape').strip(). replace('}', '\n')
        return cookie, lines.split('\n')
