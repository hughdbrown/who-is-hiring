#!/usr/bin/env python3
from pathlib import Path

import click

import get_config

@click.command()
@click.option('-y', '--year', required=False, type=str)
@click.option('-m', '--month', required=False, type=str)
def main(year=None, month=None):
    year = year or "20*"
    month = month or "*"

    config_dir: Path = get_config.cache_dir()
    globs = [
        f"hacker-news-{year}-{month}-01.txt",
        f"hacker-news-{year}-{month}-01.json",
    ]
    for glob in globs:
        for p in sorted(config_dir.glob(glob)):
            print(f"Deleting {str(p)}")
            p.unlink()


if __name__ == '__main__':
    main()
