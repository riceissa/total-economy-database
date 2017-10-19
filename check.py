#!/usr/bin/env python3

import re
import glob


SCRIPTS = glob.glob("proc_*.py")


def squeeze_hyphens(s):
    return "_".join(filter(bool, s.split('-')))


def scriptnames(url):
    filename = url.split('=')[1].split('&')[0]
    root = filename.split('.')[0]

    if "MAY" in root or "NOV" in root:
        return [
            "proc_" + root + "_adjusted.py",
            "proc_" + root + "_original.py",
        ]
    else:
        return ["proc_" + squeeze_hyphens(root) + ".py"]


def check_url(url):
    for s in scriptnames(url):
        assert s in SCRIPTS, url

        with open(s, "r") as f:
            for line in f:
                if line.startswith("with open"):
                    check_csv(line, url, s)
                elif "www.conference-board.org" in line:
                    check_dl_link(line, url, s)
                elif line.startswith("fps ="):
                    check_glob_csv(line, url, s)


def check_csv(line, url, scriptname):
    csv = scriptname.replace(".py", ".csv").replace("proc_", "")
    assert csv in line, (scriptname, csv, line)


def check_dl_link(line, url, scriptname):
    assert url in line, (scriptname, url, line)


def check_glob_csv(line, url, scriptname):
    filename = url.split('=')[1].split('&')[0]
    root = filename.split('.')[0]
    assert root in line, (scriptname, root, line)


if __name__ == "__main__":
    with open("urls", "r") as f:
        for line in f:
            url = line.strip()
            check_url(url)
    print("Done.")
