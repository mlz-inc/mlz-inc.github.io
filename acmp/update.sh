#!/usr/bin/env bash
echo "Parsing table..."

path=$( git rev-parse --show-toplevel )
python $path/acmp/parser_top.py > $path/acmp/real_table_source.org

emacs $path/acmp/real_table.org  --batch -f org-html-export-to-html --kill
git add $path/acmp/real_table.org $path/acmp/real_table.html
git commit -m "Table updating"
git push
