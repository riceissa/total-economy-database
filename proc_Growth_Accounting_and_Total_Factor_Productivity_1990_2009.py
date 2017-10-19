#!/usr/bin/env python3

import csv
import sys
import re
import glob

from util import *


def do_reader(reader, metric):
    insert_line = "insert into data(region, year, database_url, data_retrieval_method, metric, units, value, notes) values"
    count = 0
    first = True
    for row in reader:
        for region in sorted(row):
            if region and row[region] and region != 'Year':
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(region),  # region
                    mysql_int(row['Year']),  # year
                    mysql_quote("https://www.conference-board.org/retrievefile.cfm?filename=Growth-Accounting-and-Total-Factor-Productivity-1990-2009.xls&type=subsite"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(metric),  # metric
                    mysql_quote(""),  # units
                    mysql_float(row[region]),  # value
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


fps = glob.glob("../total-economy-database-data/Growth-Accounting-and-Total-Factor-Productivity-1990-2009.*.csv")

for fp in fps:
    metric = fp.split('.')[-2]
    with open(fp, newline='') as f:
        reader = csv.DictReader(f)
        do_reader(reader, metric)