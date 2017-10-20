#!/usr/bin/env python3

import csv
import sys
import re

from util import *


insert_line = "insert into data(region, year, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("../total-economy-database-data/TED_REGIONS_NOV20161_original.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        for year in range(1990, 2017):
            y = str(year)
            if row[y]:
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(row['REGION']),  # region
                    mysql_int(y),  # year
                    mysql_quote("https://www.conference-board.org/retrievefile.cfm?filename=TED_REGIONS_NOV20161.xlsx&type=subsite"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(row['INDICATOR'] + " (original)"),  # metric
                    mysql_quote(row['MEASURE']),  # units
                    mysql_float(row[y]),  # value
                    mysql_quote(""),  # notes
                ]) + ")")
                first = False
                count += 1
                if count > 5000:
                    count = 0
                    first = True
                    print(";")
    if not first:
        print(";")
