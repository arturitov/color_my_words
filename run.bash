#!usr/local/bash

while true
do
	python alchemyapi.py 1965c860662b3ec66ee989b20323f5473e9fa89b
	python scrape_article.py news | tee txt/new.txt
	python scrape_article.py lyrics | tee txt/lycs.txt
	cat txt/new.txt >> txt/log.txt
	cat txt/new.txt
	echo "Sleeping..."
	sleep 14000
done
