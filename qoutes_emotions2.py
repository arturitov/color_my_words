import pickle
import random
import words

def main(): 
	chain = pickle.load(open("obj/chain.p", "rb"))
	tweets = 0 
	found = False
	top_hit = False
	top_word, frequency ,emotion_list= words.map_words()
	srr = ""
	qoute = ""
	t1 = False
	t2 = False

	print "Frequency Dic:"
	print frequency
	print
	print "Emotion List:"
	print emotion_list

	wfound = []

	if len(emotion_list) < 2:
		print "\nNot enough emotions were mapped."
		print "Skipping article!!!!\n"
	

	while not top_hit and top_word != '' and tweets <=100000 and len(emotion_list) >= 2:
		new_review = []
		sword1 = "BEGIN"
		sword2 = "NOW"
		 
		while True:
		    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
		    if sword2 == "END":
		        break
		    new_review.append(sword2)
		 
		if len(' '.join(new_review)) <= 70 and len(' '.join(new_review)) >= 30:
			qoute = ' '.join(new_review)
			count = 0
			srr = ""
			for x in xrange(0, len(qoute)):
				if qoute[x] == "," or qoute[x] == "\"" or qoute[x] == ".":
					srr += " "
				elif qoute[x] == '\xe2'or qoute[x] == '\x80' or qoute[x] =='\x9c' or qoute[x] == '\x9d':
					srr += ""
				else:
					srr += qoute[x]

			t1 = False
			t2 = False
			for word in srr.split(' '):
				if word in frequency[emotion_list[0]]['rw']:
					wfound.append(word)
					t1 = True
				if word in frequency[emotion_list[1]]['rw']:
					wfound.append(word)
					t2 = True
				if t1 or t2:
					top_hit = True
					print
					print qoute
					print
					break
	
			tweets +=1


	return qoute


if __name__ == '__main__':   
     main()