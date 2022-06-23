#!/usr/bin/env bash
echo "Launches a map in the browser using an address from the command line or clipboard."
echo -n "> "
read ANYTHING
python3 ~/repos/ATBS_exercises/chapter_11-mapit/mapIt.py $ANYTHING

