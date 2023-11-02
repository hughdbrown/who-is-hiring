#!/usr/bin/env python3
from pathlib import Path
import re

import click

import get_config

RUST_RE = re.compile(r'''([^a-z]rust[^a-z])''', re.IGNORECASE)
DATE_RE = re.compile(r'''(\d{4}-\d{2}-\d{2})''')

# from whyslow import profile


def process_child(text, items, company_re, i):
    if (m := RUST_RE.search(text)):
        if company_re:
            if company_re.search(text):
                #print(text)
                items.append(text)
        else:
            first_line = text.splitlines()[0]
            items.append((f"{i} {first_line[:100]}"))


@click.command()
@click.option('-c', '--company', required=False, type=str)
# @profile()
def main(company=None):
    company_re = (
        re.compile(fr'''\b{company}\b''', re.IGNORECASE) if company
        else None
    )

    config_dir: Path = get_config.cache_dir()
    for p in sorted(config_dir.glob("hacker-news-*.txt")):
        date = DATE_RE.search(str(p)).group(1)
        with p.open("r", encoding="utf-8") as handle:
            children = handle.readlines()
            items = [
                f"{'-' * 20} {date} {p.name}: {len(children)}",
            ]
            for i, text in enumerate(children):
                text = text.replace("\t", "\n")
                process_child(text, items, company_re, i)
            if len(items) > 1:
                print("\n".join(items))

    #for k, v in sorted(d.items()):
    #    for p in sorted(v):
    #        print(f"{k} {p}")


if __name__ == '__main__':
    main()
