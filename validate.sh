#!/bin/bash

# This script runs doctests on all Markdown files in the current directory and its subdirectories.
# It ignores Markdown files in the 3_API directory. This documentation is auto-generated from the Python docs, which is
# tested by the source package.
find "$(dirname "$0")" -type f -name "*.md" | while read -r file; do
    if [[ "$file" == */3_API/* ]]; then
        continue
    fi
    echo "Testing $file"
    python -m doctest "$file"
    if [ $? -ne 0 ]; then
        echo "Doctest failed for $file"
        exit 1
    fi
done
