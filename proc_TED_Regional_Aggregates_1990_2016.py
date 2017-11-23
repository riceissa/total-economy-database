#!/usr/bin/env python3

import csv
import sys
import re
import glob

from devec_sql_common import *


def do_reader(reader, metric):
    insert_line = "insert into data(region, odate, database_url, data_retrieval_method, metric, units, value, notes) values"
    count = 0
    first = True
    for row in reader:
        for year in range(1990, 2017):
            y = str(year)
            if row[y]:
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(row['Country / Region']),  # region
                    mysql_string_date(y),  # odate
                    mysql_quote("https://www.conference-board.org/retrievefile.cfm?filename=TED---Regional-Aggregates-1990-2016.xlsx&type=subsite"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(metric),  # metric
                    mysql_quote(""),  # units
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


fps = glob.glob("../total-economy-database-data/TED---Regional-Aggregates-1990-2016.*.csv")

for fp in fps:
    metric = fp.split('.')[-2]
    with open(fp, newline='') as f:
        reader = csv.DictReader(f)
        do_reader(reader, metric)
