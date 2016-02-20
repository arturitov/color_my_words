import pickle
import random
 
chain = pickle.load(open("chain.p", "rb"))
tweets = 0 

while tweets <10:
	pass
	new_review = []
	sword1 = "BEGIN"
	sword2 = "NOW"
	 
	while True:
	    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
	    if sword2 == "END":
	        break
	    new_review.append(sword2)
	 
	if len(' '.join(new_review)) <= 140 and len(' '.join(new_review)) >= 40:
		qoute = ' '.join(new_review)
		count = 0
		srr = ""
		for x in xrange(0, len(qoute)):
			if qoute[x] == "," or qoute[x] == "\"" or qoute[x] == "." or qoute[x] == '\xe2\x80\x9c':
				srr += " "
			elif x == 0 or x == 1 or x == 2:
				srr += ""
			elif x ==len(qoute)-1 or x ==len(qoute)-2 or x ==len(qoute)-3:
				srr += ""
			else:
				srr += qoute[x]
				# print x, srr
		print srr
		print qoute
				
		tweets +=1