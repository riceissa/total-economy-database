#!/usr/bin/env python3

import csv
import sys
import re
import glob

from devec_sql_common import *

print_insert_header()


def do_reader(reader, metric):
    insert_line = "insert into data(region, odate, database_url, data_retrieval_method, metric, units, value, notes) values"
    count = 0
    first = True
    for row in reader:
        for region in sorted(row):
            if region and row[region] and region != 'Year':
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + uniq_join([
                    mysql_quote(region_normalized(region)),  # region
                    mysql_string_date(row['Year']),  # odate
                    mysql_quote("https://www.conference-board.org/retrievefile.cfm?filename=Output-Labor-and-Labor-Productivity-1950-2013.xls&type=subsite"),  # database_url
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


fps = glob.glob("../total-economy-database-data/Output-Labor-and-Labor-Productivity-1950-2013.*.csv")

for fp in fps:
    metric = fp.split('.')[-2]
    with open(fp, newline='') as f:
        reader = csv.DictReader(f)
        do_reader(reader, metric)


print_insert_footer()
