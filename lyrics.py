import bs4
import requests
import sys
import qoutes_emotions2 as qoutes
import tinyurl
import time
import tweet
import save_load_obj as slo
from random import randint


urls = list()
titles = list()
url = "http://www.metrolyrics.com/top100.html"
r = requests.get(url) 
soup = bs4.BeautifulSoup(r.text,"html.parser") 
html = ""
top_20 = soup.find('ul',{"class":"top20"})
for song in top_20.find_all('span',{"class":"song"}):
	for box in song.find_all('a'):
		try:
			if box['href'] not in urls and box['href'].endswith('html') and "song-link" in box['class']:
				urls.append(box['href'])
				print "---------------------------"
				print box['href']
				for v in box:
					title = str(v).strip()
					print title
		except:
			pass
	for artist in song.find_all('span',{"class":"artist"}):
		try:
			# print vars(artist)
			for a in artist:
				for aa in a:
					if len(aa) > 3:
						arts = str(aa).strip().strip()
						print arts 
		except:
			pass
	title = arts + " - " + title
	title = title[:title.find("Lyrics")-1]
	titles.append(title)