#!/usr/bin/env python3
from collections import defaultdict
import json
from pathlib import Path
from pprint import pprint
import re

from bs4 import BeautifulSoup
import click

RUST_RE = re.compile(r'''([^a-z]rust[^a-z])''', re.IGNORECASE)
DATE_RE = re.compile(r'''(\d{4}-\d{2}-\d{2})''')


@click.command()
@click.option('-c', '--company', required=False, type=str)
def main(company=None):
    d = defaultdict(set)
    if company:
        print(f"Searching for '{company}'")
        company_re = re.compile(fr'''\b{company}\b''', re.IGNORECASE)
    for p in sorted(Path().home().glob("hacker-news-*.json")):
        date = DATE_RE.search(str(p)).group(1)
        with p.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
            print(f"{'-' * 20} {date} {p.name}: {len(data['children'])}")
            for i, child in enumerate(data["children"]):
                text = child['text']
                if text is not None:
                    soup = BeautifulSoup(text, "lxml")
                    text = " ".join(soup.find_all(text=True))
                    if (m := RUST_RE.search(text)):
                        if company:
                            if company_re.search(text):
                                print(text)
                        else:
                            first_line = text.splitlines()[0]
                            print(f"{i} {first_line[:100]}")
                        match = m.group(1)
                        d[match].add(str(p))

    #for k, v in sorted(d.items()):
    #    for p in sorted(v):
    #        print(f"{k} {p}")


if __name__ == '__main__':
    main()
