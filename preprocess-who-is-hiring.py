#!/usr/bin/env python3
import json
import logging
import os
from pathlib import Path
import re

from bs4 import BeautifulSoup

import get_config

DATE_RE = re.compile(r'''(\d{4}-\d{2}-\d{2})''')
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    # logger levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL
    level=os.environ.get('LOGLEVEL', 'INFO').upper(),
)
logger = logging.getLogger()

# from whyslow import profile

def all_text(text):
    soup = BeautifulSoup(text, "lxml")
    return " ".join(soup.find_all(string=True))


# @profile()
def main():
    config_dir:Path = get_config.cache_dir()
    for path_in in sorted(config_dir.glob("hacker-news-*.json")):
        date = DATE_RE.search(str(path_in)).group(1)
        with path_in.open("r", encoding="utf-8") as handle:
            logger.debug(f"Reading {str(path_in)}")
            data = json.load(handle)
            path_out = path_in.with_suffix(".txt")
            children = data['children']
            print(f"{date}: {len(children)} listings")

            if not path_out.exists():
                logger.debug(f"Writing {str(path_out)}")
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
