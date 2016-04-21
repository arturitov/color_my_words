#!/bin/bash

FILES=$1'/*'
DEST=$2
count=0
for f in $FILES; do
	counter=$((counter+1))
	mv $f $DEST"/image"$counter".png"
done