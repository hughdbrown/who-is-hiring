#!/usr/bin/env python3

from collections import defaultdict
import re
import sys

def make_display(co_dates, dates):
    display = []
    i = 0
    for date in dates:
        if i < len(co_dates) and date == co_dates[i]:
            display.append('X')
            i += 1
        else:
            display.append('.')
    return "".join(display)

def main():
    co_reg = re.compile(r'''^\d+ ([^|]+)|''')
    date_reg = re.compile(r'^[-]+ ([0-9-]+)')
    companies = defaultdict(list)
    current_date, dates = None, []

    for line in sys.stdin:
        if (m := date_reg.match(line)):
            current_date = m.groups(1)[0]
            dates.append(current_date)
        elif current_date and (m := co_reg.match(line)):
            company = m.groups(1)[0].strip()
            companies[company].append(current_date)

    for (co, co_dates) in sorted(companies.items()):
        display = make_display(co_dates, dates)

        # If the company name is longer than 50 characters, likely it is filled in wrong
        print(f"{''.join(display)} {co[:50]}")


if __name__ == '__main__':
    main()
