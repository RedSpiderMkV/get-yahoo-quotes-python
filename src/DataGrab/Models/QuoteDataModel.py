#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:22:48 2019

@author: nikeah
"""

class QuoteDataModel:
    def __init__(self, date, openValue, highValue, lowValue, closeValue, adjustedClose, volumeValue):
        self.Date = date
        self.Open = openValue
        self.High= highValue
        self.Low = lowValue
        self.Close = closeValue
        self.AdjustedClose = adjustedClose
        self.Volume = volumeValue

    
    def PrintData(self):
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (self.Date, self.Open, self.High, self.Low,
                                         self.Close, self.AdjustedClose, self.Volume))
