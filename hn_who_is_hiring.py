#!/usr/bin/env python3
import json
from pathlib import Path

import requests

IDS = {
    37351667: {"date": "2023-09-01"},
    36956867: {"date": "2023-08-01"},
    36573871: {"date": "2023-07-01"},
    36152014: {"date": "2023-06-01"},
    35773707: {"date": "2023-05-01"},
    35424807: {"date": "2023-04-01"},
    34983767: {"date": "2023-03-01"},
    34612353: {"date": "2023-02-01"},
    34219335: {"date": "2023-01-01"},
    33818037: {"date": "2022-12-01"},
    33422129: {"date": "2022-11-01"},
    33068421: {"date": "2022-10-01"},
    32677265: {"date": "2022-09-01"},
    32306920: {"date": "2022-08-01"},
    31947297: {"date": "2022-07-01"},
    31582796: {"date": "2022-06-01"},
    31235968: {"date": "2022-05-01"},
    30878761: {"date": "2022-04-01"},
    30515750: {"date": "2022-03-01"},
    30164271: {"date": "2022-02-01"},
    29782099: {"date": "2022-01-01"},
    29405056: {"date": "2021-12-01"},
    29067493: {"date": "2021-11-01"},
    28719320: {"date": "2021-10-01"},
    28380661: {"date": "2021-09-01"},
    28037366: {"date": "2021-08-01"},
    27699704: {"date": "2021-07-01"},
    27355392: {"date": "2021-06-01"},
    27025922: {"date": "2021-05-01"},
    26661443: {"date": "2021-04-01"},
    26304051: {"date": "2021-03-01"},
    25989764: {"date": "2021-02-01"},
    25632982: {"date": "2021-01-01"},
}


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
