from alchemyapi import AlchemyAPI
import operator
import collections 
import copy
import string



def main(text):
	alchemyapi = AlchemyAPI()
	if text == 'news':
		with open('txt/article.txt', 'r') as myfile:
			data=myfile.read()
	elif text == "lyrics":
		with open('txt/lyrics.txt', 'r') as myfile:
			data=myfile.read()
	# with open('txt/article_test.txt', 'r') as myfile_test:
	# 	data_test=myfile_test.read()

	response = alchemyapi.emotion("text", data)
	# print response
	# response_test =alchemyapi.emotion("text", data_test)

	emotion_list = list()
	maxs = 0
	print "Overall"
	for e in response['docEmotions']:
		print e, response['docEmotions'][e]
		if float(response['docEmotions'][e]) > maxs:
			maxs = float(response['docEmotions'][e])
			max_emotion = e
	emotion_list.append(max_emotion)
	if not maxs >0.4:
		maxs = 0
		for e in response['docEmotions']:
			# print e, response['docEmotions'][e]
			if float(response['docEmotions'][e]) > maxs and float(response['docEmotions'][e]) < float(response['docEmotions'][emotion_list[0]]):
				maxs = float(response['docEmotions'][e])
				max_emotion = e
		emotion_list.append(max_emotion)

	exclude = set(['#', '"', '%' , '&', ')', '(', '+', '*', '-', ',', '/', '.', ';', ':', '=', '<', '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}', '|', '~'])
	sentence = data.split('\n')

	emotions = dict()
	emot_freq =  dict()
	emot_freq_2 = dict()
	sentences = dict()

	if text != "":
		for s in sentence:
			# print s
			s = ''.join(ch for ch in s if ch not in exclude)

			# print s

			if len(s) < 10:
				continue

			if s in sentences:
				# print "found"
				response = sentences[s]
			else:
				response = alchemyapi.emotion("text", s)
			try:
				# print response['docEmotions']
				max_emotion = max(response['docEmotions'].iteritems(), key=operator.itemgetter(1))[0]
			except Exception, e:
				continue
			
			# print max_emotion


			if max_emotion not in emot_freq:
					emot_freq_2[max_emotion] = 0
			emot_freq_2[max_emotion] += 1

			if float(response['docEmotions'][max_emotion]) >= 0.35:
				# print max_emotion
				if max_emotion not in emot_freq:
					emot_freq[max_emotion] = 0
				if str(max_emotion) == 'disgust' and float(response['docEmotions'][max_emotion]) < 0.5:
					continue
				emot_freq[max_emotion] += 1
				# if max_emotion == 'disgust':
				# 	print "------------->",s

			sentences[s] = response


		for e in emot_freq:
		     print e,emot_freq[e]
		print
		print "----test------"
		for e in emot_freq_2:
		     print e,emot_freq_2[e]
		print "----test------"

		emot_freq_3 = copy.deepcopy(emot_freq)
		emotion_list = list()
		max_emotion = max(emot_freq.iteritems(), key=operator.itemgetter(1))[0]
		emotion_list.append(str(max_emotion))
		emot_freq[max_emotion] = 0
		max_emotion = max(emot_freq.iteritems(), key=operator.itemgetter(1))[0]
		emotion_list.append(str(max_emotion))

		if emot_freq_3[emotion_list[0]] >= 2*emot_freq_3[emotion_list[1]] :
			emotion_list = emotion_list[0:1]


	print emotion_list

	if emotion_list[0] == 'joy' and 'disgust' in emotion_list:
		emotion_list = ['joy']	

	return emotion_list

if __name__ == '__main__':   
	main()
# for emotion in emotions:
# 	print emotion, emotions[emotion]
# 	print sum(emotions[emotion])/len(emotions[emotion])


# anger 0.028377
# joy 0.005032
# fear 0.008352
# sadness 0.204989
# disgust 0.305384
