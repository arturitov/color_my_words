#from nltk.corpus import wordnet as wn
import sys
import pickle
import save_load_obj as slo



def what_tense(word):
	if word != "":
		if word[-1]== 'g' and word[-2] == 'n' and word[-3] == 'i':
			return "present-perfect"
		elif word[-1]== 'd' and word[-2] == 'e':
			return "past"
		else:
			return "present"

def past2present(word):
	srr = ""
	for w in xrange(0,len(word)-2):
		srr += word[w]
	return [srr, srr + 'e']

def past2present_perf(word):
	srr = ""
	for w in xrange(0,len(word)-2):
		srr += word[w]
	return [srr + "ing"]

def present2past(word):
	srr = word
	return [srr + "ed"]

def present2present_perf(word):
	srr = word
	return [srr + "ing"]

def present_perf2present(word):
	srr = ""
	for w in xrange(0,len(word)-3):
		srr += word[w]
	return [srr]

def present_perf2past(word):
	srr = ""
	for w in xrange(0,len(word)-3):
		srr += word[w]
	return [srr + "ed"]	

def open_article(file):
	fh = open(file, "r")
	string = ""
	for line in fh.readlines():
		string += line
	return string

def remove_punct(string):
	srr = ""
	for x in xrange(0, len(string)):
		if string[x] == "," or string[x] == "\"" or string[x] == ".":
			srr += " "
		elif string[x] == '\xe2'or string[x] == '\x80' or string[x] =='\x9c' or string[x] == '\x9d':
			srr += ""
		else:
			srr += string[x]
	return srr

def map_words():

	# Load word : synonym dictionary
	words = dict()
	words = slo.load_obj("obj/rel_words2")

	string = open_article("txt/article.txt")
	string = remove_punct(string)

	frequency = {}

	# Attemps to map each word in text to a word in the words dictionary
	for word_s in string.split(" "):
		word_list = []
		word_list.append(word_s)
		for word in word_list:
			
			if word != 'still':
				word = word.lower()

				for emotion in words:
					# if word equals emotion then it found an exact match of an emotion
					# we were looking for so it adds it to frequency and gives it a weight
					# of 3 (the highest because it was an excact match)
					if word == emotion:
						if frequency.has_key(emotion):
							frequency[emotion]["rw"].append(word)
							frequency[emotion]["weight"] += 3
							continue
						else:
							frequency[emotion] = dict()
							frequency[emotion]["rw"] = [word]
							frequency[emotion]["weight"] = 0
							frequency[emotion]["weight"] += 3
							continue

					# word found is a synonym of the emotion we are looking for		
					if words[emotion].has_key(word):
						if frequency.has_key(emotion):
							frequency[emotion]["rw"].append(word)
							frequency[emotion]["weight"] += 2
							continue
						else:
							frequency[emotion] = dict()
							frequency[emotion]["rw"] = [word]
							frequency[emotion]["weight"] = 0
							frequency[emotion]["weight"] += 2
							continue

					for s in words[emotion]:
						# word found is a synonym  of a synononym of the emotion we are looking for	
						if words[emotion][s].has_key(word):
							if frequency.has_key(emotion):
								frequency[emotion]["rw"].append(word)
								frequency[emotion]["weight"] += 1
								continue
							else:
								frequency[emotion] = dict()
								frequency[emotion]["rw"] = [word]
								frequency[emotion]["weight"] = 0
								frequency[emotion]["weight"] += 1
								continue
					

	# Which emotional word has the most hits
	max = 0
	top_hit = ""
	for emotion in frequency:
		if frequency[emotion]['weight'] >= max:
			top_hit = emotion
			max = frequency[emotion]['weight']

	emotion_list = list()

	if len(frequency) == 0:
		return top_hit, frequency, []
		pass
	else:
		# emotion_list contains the emotions that were found with the highest weight first
		emotion_list = (sorted(frequency, key=lambda k: frequency[k]['weight'], reverse=True))
		return top_hit, frequency, emotion_list


if __name__ == '__main__':   
     map_words()

