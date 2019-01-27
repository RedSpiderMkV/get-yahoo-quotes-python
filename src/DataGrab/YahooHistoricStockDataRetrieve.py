#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:33:25 2019

@author: nikeah
"""


import sys


from Utils.EpochTimeRetriever import EpochTimeRetriever
from DataManagement.CsvDataRetriever import CsvDataRetriever
from DataManagement.CsvDataParser import CsvDataParser
from Models.QuoteDataModel import QuoteDataModel
    

def main():
    csvDataRetriever = CsvDataRetriever()
    epochTimeRetriever = EpochTimeRetriever()
    
    startDate = epochTimeRetriever.GetTime('1970-01-01')
    endDate = epochTimeRetriever.GetToday()

    if len(sys.argv) == 1:
        print("\nUsage: get-yahoo-quotes.py SYMBOL [optional yyyy-mm-dd]START_DATE [optional yyyy-mm-dd]END_DATE\n\n")
        return
    
    symbol = sys.argv[1]    
    if len(sys.argv) > 2:
        startDate = epochTimeRetriever.GetTime(sys.argv[2])
    
    if len(sys.argv) > 3:
        endDate = epochTimeRetriever.GetTime(sys.argv[3])
    
    print("Downloading Data: %s" % (symbol))
    csvData = csvDataRetriever.GetQuotes(symbol, startDate, endDate)
    
    csvDataParser = CsvDataParser()
    dataModelCollection = csvDataParser.GetModelsFromCsv(csvData)
    
    [x.PrintData() for x in dataModelCollection]


if __name__ == '__main__':
    print("--------------------------------------------------")
    main()
