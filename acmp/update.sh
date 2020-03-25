#!/usr/bin/env bash
echo "Parsing table..."
path=$( git rev-parse --show-toplevel )
python $path/acmp/parser_top.py > $path/acmp/real_table_source.org 
