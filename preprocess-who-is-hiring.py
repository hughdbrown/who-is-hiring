#!/usr/bin/env python3
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup

DATE_RE = re.compile(r'''(\d{4}-\d{2}-\d{2})''')

# from whyslow import profile

def all_text(text):
    soup = BeautifulSoup(text, "lxml")
    return " ".join(soup.find_all(text=True))


# @profile()
def main():
    for path_in in sorted(Path().home().glob("hacker-news-*.json")):
        date = DATE_RE.search(str(path_in)).group(1)
        with path_in.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
            path_out = path_in.with_suffix(".txt")
            children = data['children']
            print(f"{date}: {len(children)} listings")

            if not path_out.exists():
                with path_out.open("w", encoding="utf-8") as out:
                    out.write(
                        "\n".join(
                            all_text(text).replace("\t", "").replace("\n", "\t")
                            for child in children
                            if (text := child['text']) is not None
                        )
                    )

if __name__ == '__main__':
    main()
