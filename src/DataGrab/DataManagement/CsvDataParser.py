#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:21:12 2019

@author: nikeah
"""

from Models.QuoteDataModel import QuoteDataModel


DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
ADJUSTED_CLOSE = 5
VOLUME = 6

CSV_FIELD_COUNT = 7

class CsvDataParser:
    
    def GetModelsFromCsv(self, csvData):
        quoteDataCollection = [self._getModelFromCsv(data) for data in csvData[1:]]
        
        return filter(lambda data: data is not None, quoteDataCollection)
    
    
    def _getModelFromCsv(self, csvData):
        csvComponents = csvData.rstrip().split(',')
        
        if len(csvComponents) != CSV_FIELD_COUNT:
            return None
        
        quoteDataModel = QuoteDataModel(
                csvComponents[DATE],
                csvComponents[OPEN],
                csvComponents[HIGH],
                csvComponents[LOW],
                csvComponents[CLOSE],
                csvComponents[ADJUSTED_CLOSE],
                csvComponents[VOLUME])
        
        return quoteDataModel
