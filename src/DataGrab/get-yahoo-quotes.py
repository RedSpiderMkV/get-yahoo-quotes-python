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


import sys


from Utils.EpochTimeRetriever import EpochTimeRetriever
from DataManagement.CsvDataRetriever import CsvDataRetriever


def write_data_to_file(filename, content_data_lines):
    with open (filename, 'w') as handle:
        for line in content_data_lines:
            handle.write(line + '\n')
    

def main():
    csv_data_retriever = CsvDataRetriever()
    epoch_time_retriever = EpochTimeRetriever()
    
    start_date = epoch_time_retriever.GetTime('1970-01-01')
    end_date = epoch_time_retriever.GetToday()

    if len(sys.argv) == 1:
        print("\nUsage: get-yahoo-quotes.py SYMBOL [optional yyyy-mm-dd]START_DATE [optional yyyy-mm-dd]END_DATE\n\n")
        return
    
    symbol = sys.argv[1]    
    if len(sys.argv) > 2:
        start_date = epoch_time_retriever.GetTime(sys.argv[2])
    
    if len(sys.argv) > 3:
        end_date = epoch_time_retriever.GetTime(sys.argv[3])
    
    print("Downloading Data: %s" % (symbol))
    csv_data = csv_data_retriever.GetQuotes(symbol, start_date, end_date)
    
    print("Writing Data: %s to %s.csv" % (symbol, symbol))
    filename = '%s.csv' % (symbol)
    write_data_to_file(filename, csv_data)


if __name__ == '__main__':
    print("--------------------------------------------------")
    main()
