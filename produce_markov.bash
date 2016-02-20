#!/bin/bash


# capture output of script
python parse.py >> qoute.txt

# add the words "BEGIN NOW" to the beginning of each line
cat qoute.txt | sed 's/^/BEGIN NOW /' > prep3.txt

# add the word "END" to the end of each line
cat prep3.txt | sed 's/$/ END/' > inspiration.txt

python markov.py