#!/usr/bin/env bash
echo "multi clipboard manual: "
echo "save <keyword> - Saves clipboard to keyword."
echo "<keyword> - Loads keyword to clipboard."
echo "list - Loads all keywords to clipboard."
echo -n "> "
read ANYTHING
python3 ~/repos/ATBS_exercises/chapter_09-Multi_Clipboard/mcb.pyw $ANYTHING