#!/usr/bin/env python3
import json
from pathlib import Path

import requests

from data import IDS

def main():
    headers = {'Accept': 'application/json'}

    def get_data(date):
        url = f"https://hn.algolia.com/api/v1/items/{_id}"
        req = requests.get(url, headers=headers)
        return req.json()

    def write_data(data, date):
        pj = Path().home().joinpath(f"hacker-news-{date}.json")
        if not pj.exists():
            with pj.open("w", encoding="utf-8") as handle:
                json.dump(data, handle, sort_keys=True, indent=4)

    for _id, val  in IDS.items():
        date = val['date']
        data = get_data(date)
        print(f"{date}: {len(data['children'])} listings")
        write_data(data, date)


if __name__ == '__main__':
    main()
