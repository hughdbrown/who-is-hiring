#!/usr/bin/env python3
import json
from pathlib import Path
from pprint import pprint
import re

from bs4 import BeautifulSoup

def main():
    rust_re = re.compile(r'''\brust\b''', re.IGNORECASE)
    # Formatting is not reliable enough to extract company name
    # company_re = re.compile(r'''^\<p\>(.*?)\|''')
    first_line_re = re.compile(r'''^\<p\>(.*?)\<\/p\>''')
    date_re = re.compile(r'''(\d{4}-\d{2}-\d{2})''')
    for p in sorted(Path().home().glob("hacker-news-*.json")):
        date = date_re.search(str(p)).group(1)
        print(f"{'-' * 20} {date}")
        with p.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
            print(f"{p.name}: {len(data['children'])}")
            for i, child in enumerate(data["children"]):
                text = child['text']
                if text is not None:
                    if rust_re.search(text):
                        # c = company_re.search(text)
                        # d[c].append(date)
                        soup = BeautifulSoup(text, "lxml")
                        # re_result = first_line_re.search(text)
                        first_line = (" ".join(soup.find_all(text=True))).splitlines()[0]
                        print(f"{i} {first_line}")


if __name__ == '__main__':
    main()
