# Purpose
Download the monthly "Who Is Hiring?" posts from Hacker News. Use the JSON feed instead of extracting HTML.

## hn_who_is_hiring.py 
Pull down data from the JSON feed, store to disk.

## preprocess-who-is-hiring.py
Open each cached JSON file, convert to one job per line with newlines in the `.["children"]["text"]` converted to tabs.

## extract-who-is-hiring.py
Open each text file and scan for terms of interest. In this case, I was interested in finding companies that had ever advertised positions that use the Rust programming language. This code is representative of what needs to be done for any search.

