#!/usr/bin/env python3
"""Scrape Hacker News for "Who Is Hiring?" posts."""
import json
import logging
import os
from pathlib import Path
from typing import Any, Dict

import requests

import get_config

from data import IDS

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    # logger levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL
    level=os.environ.get('LOGLEVEL', 'INFO').upper(),
)
logger = logging.getLogger()

def main():
    """Main entry point for downloading Who Is Hiring data"""

    def get_data(article_id: int):
        """Read "Who Is Hiring?" posts for a month from Hacker News."""
        headers = {'Accept': 'application/json'}
        url = f"https://hn.algolia.com/api/v1/items/{article_id}"
        req = requests.get(url, headers=headers)
        return req.json()

    def write_data(data: Dict[str, Any], pj: Path):
        """Write JSON for month of "Who Is Hiring?" to root."""
        with pj.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, sort_keys=True, indent=4)

    config_dir: Path = get_config.cache_dir()
    logger.debug(f"Saving data to {config_dir}")

    for article_id, date in IDS.items():
        pj: Path = config_dir.joinpath(f"hacker-news-{date}.json")
        if not pj.exists():
            logger.debug(f"Pulling data for {date}")
            data = get_data(article_id)
            print(f"{date}: {len(data['children'])} listings")
            write_data(data, pj)


if __name__ == '__main__':
    main()
