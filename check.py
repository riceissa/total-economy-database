#!/usr/bin/env python3

import re
import glob


SCRIPTS = glob.glob("proc_*.py")


def squeeze_hyphens(s):
    s = "_".join(filter(bool, s.split('-')))
    return s

def check_url(url):
    filename = url.split('=')[1].split('&')[0]
    root = filename.split('.')[0]

    if "MAY" in root or "NOV" in root:
        scriptname = "proc_" + root + "_adjusted.py"
    else:
        scriptname = "proc_" + squeeze_hyphens(root) + ".py"

    assert scriptname in SCRIPTS, filename


if __name__ == "__main__":
    with open("urls", "r") as f:
        for line in f:
            url = line.strip()
            check_url(url)
    print("Done.")
