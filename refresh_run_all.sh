#!/bin/sh

YEAR=${1:2024}
MONTH=${2:01}
./refresh_hn_data.py --year $YEAR --month $MONTH

./hn_who_is_hiring.py
./preprocess-who-is-hiring.py
./extract-rust-postings.py
