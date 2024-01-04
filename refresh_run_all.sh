#!/bin/sh

YEAR=${1}
MONTH=${2}
./refresh_hn_data.py --year=$YEAR --month=$MONTH

./hn_who_is_hiring.py
./preprocess-who-is-hiring.py
./extract-rust-postings.py
