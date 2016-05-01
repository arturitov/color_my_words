import tweepy, time, sys
import image
import get_emotion
import qoutes_emotions2 as qoutes


def main(tinyurl, title,text):
	CONSUMER_KEY = 'J7X45HzXdZCvTBmcB3wCPOvcx'#keep the quotes, replace this with your consumer key
	CONSUMER_SECRET = 'zm3BYXDZnw9jwNIK4VX3pIrpZj10OrDVJo2XMFLG81ARF8GpzV'#keep the quotes, replace this with your consumer secret key
	ACCESS_KEY = '723627685193228288-LkMh35QxeQrAXk5Pr0QwLpAOY9rlcxG'#keep the quotes, replace this with your access token
	ACCESS_SECRET = '79SZyLhpB9opYXRZbnid5tvpw5YD0IExx1KGSE7gezGZK'#keep the quotes, replace this with your access token secret
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	# # Get qoute to tweet
	# print "Getting qoute..."
	# qoute = qoutes.main()

	# if len(qoute) > 0:
	
	#finds top emotion
	emotion_list = get_emotion.main(text)

	# creates a picture to tweet based on article save in txt/article.txt
	image.main(emotion_list)

	picture = "img/tweet.png"

	text = '"'+title.encode('utf-8')+'"' + '\n'  + tinyurl + ' '

	print "Tweeting...\n"

	try:
		api.update_with_media(picture, text)
		print "Success!!!!"
		return True
	except Exception,e:
		print e
		print "*******************************"
		print "	Not tweeted"
		print "*******************************"
		return False

	return False



if __name__ == '__main__':
	main('','','')