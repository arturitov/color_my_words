import tweepy, time, sys
import image
import get_emotion
import qoutes_emotions2 as qoutes


def main(tinyurl, title,text):
	CONSUMER_KEY = 'MusRk3CP2IVZ9ENFP0xcUnmZX'#keep the quotes, replace this with your consumer key
	CONSUMER_SECRET = 'rOMBbYDP4SLXxQkfIr2BiiBWyZyjmgAo46X4SGTlxcFgo23UrU'#keep the quotes, replace this with your consumer secret key
	ACCESS_KEY = '4926558947-Femq6iBwcWsl8f9Eaau7fPp17BIkMbWNfp8kNBu'#keep the quotes, replace this with your access token
	ACCESS_SECRET = 'tbg7fDBwOhQfXFsB5irA1H0dtw4zTlNAiE4Sp1PVqqdpq'#keep the quotes, replace this with your access token secret
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

	text = title.encode('utf-8') + '...\n'  + tinyurl + ' '

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