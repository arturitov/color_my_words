
from alchemyapi import AlchemyAPI


def background_color():
	alchemyapi = AlchemyAPI()

	with open('txt/article.txt', 'r') as myfile:
	    data=myfile.read()

	response = alchemyapi.sentiment("text", data)

	score = float(response["docSentiment"]["score"])

	types = response["docSentiment"]["type"]

	print "Sentiment", types, score

	n = 140
	if score < -0.25:
		n = 0
	elif score >= -0.25 and score < 0.4:
	
		ratio = (score-(-0.4))/(.6+.4)
		n = int(n * (1+ratio) )
		if n > 220:
			n = 230
	else:
		n = 255
	print n

	# if types == "positive":
	# 	n = 255
	# elif types == "neutral":
	# 	n = 130
	# else:
	# 	n = 0

	return n