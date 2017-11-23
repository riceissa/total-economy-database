# total-economy-database

To produce the SQL file, do:

```bash
make clean  # remove file from old run in case it exists
make
```

To generate the SQL files, the scripts in this repository require the
[`devec_sql_common`](https://github.com/riceissa/devec_sql_common)
Python package.  To install, run:

```bash
git clone https://github.com/riceissa/devec_sql_common
cd devec_sql_common
pip3 install -e .
```

## License

CC0.

The data is apparently copyrighted and there's a scary disclaimer so I won't
add it to this repo. Steps to reproduce the CSVs:

1. Get the data from the [Data page](https://www.conference-board.org/data/economydatabase/index.cfm?id=27762) or the [Archive page](https://www.conference-board.org/data/economydatabase/index.cfm?id=30565)
2. Open the spreadsheet in LibreOffice.
3. Navigate to the relevant sheet.
4. Do "File" → "Save As…" and save as a CSV.
5. Remove the top few lines from the CSV (which just describe the dataset) and
   sometimes also the bottom few lines (which contain citation information) so
   that the line containing the column names is on top.
