import requests
import bs4

quotes = [] 
messages = []

for x in xrange(1,100):
	# url = "http://www.goodreads.com/quotes/tag/encouragement?page=" + str(x)
	# url = "http://www.goodreads.com/quotes/tag/inspirational-quotes?page=" + str(x)
	url = "http://www.goodreads.com/quotes/tag/happiness?page=" + str(x)
	# print url
	r = requests.get(url) 
	soup = bs4.BeautifulSoup(r.text,"html.parser") 
	for table_row in soup.select(".quoteText"):
		table_cells = table_row
		# print len(table_cells), dir(table_cells)
		# print
		# print vars(table_cells)
		# print
		for keys in table_cells:
			# print keys.encode('utf-8')
			messages.append(keys)
			break
for m in messages:
	quotes.append(' '.join(m.split()).encode('utf-8'))
# print "HHAAPPYY"
for q in quotes:
	print q




