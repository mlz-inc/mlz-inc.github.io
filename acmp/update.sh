#!/usr/bin/env bash
echo "Parsing table..."

path="/home/amder/Projects/MLZ/mlzinc.github.io"
python $path/acmp/parser_top.py > $path/acmp/real_table_source.org

echo "Exporting org to html..."
emacs $path/acmp/real_table.org  --batch -f org-html-export-to-html --kill
rm $path/acmp/real_table.html\~

echo "Pushing..."
cd $path
git add acmp/real_table.org acmp/real_table.html acmp/real_table_source.org
git commit -m "Table updating"
git push
