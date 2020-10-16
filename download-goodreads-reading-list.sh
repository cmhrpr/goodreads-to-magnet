#!/bin/bash
source .env

if [ ! -f auth.json ]; then
    bash good-reads-auth.sh
fi


SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for f in $(python extract-book-titles.py)
do
  echo "$f"
  pirate-get "$f" -c $TPB_CATEGORY_BOOKS -r 1 --download-all
done
IFS=$SAVEIFS