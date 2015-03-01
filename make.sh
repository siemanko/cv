#!/bin/sh
#!/bin/bash

# Stop on error
set -e
# Stop when undefined variable is ecountered
set -u
# Easier to debug errors
set -o pipefail

file=${1:-}
if [[ -z "$file" ]]
then
    echo "Usage $0 FILE"
    echo "Where FILE is file with your personal data."
    exit 1
fi

cd build/
rm -rf ./*
cp ../*.tex ../*.py ./ &&
cp ../$file ./cv_data.py
cp ../images/* ./ &&
xelatex cv.tex &&
pythontex --interpreter=python:/usr/bin/python3 cv.tex &&
xelatex cv.tex &&
cp cv.pdf ../
cd ..
