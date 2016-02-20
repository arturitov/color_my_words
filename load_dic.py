from wordnik import *
import sys
import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


apiUrl = 'http://api.wordnik.com/v4'
apiKey = '2b2dc4f8207d08bdea00c0e32a600fb473928170494728ec1'
client = swagger.ApiClient(apiKey, apiUrl)

wordsApi = WordsApi.WordsApi(client)
wordApi = WordApi.WordApi(client)

emotion = [
"bored",
"distracted",
"disbelief",
"distate",
"disgusted",
"disdain",
"apathetic",
"irate",
"angry",
"loathing",
"bitter",
"enraged",
"contemptuous",
"irritated",
"cranky",
"aggravated",
"upset",
"frustrated",
"hysterical",
"frantic",
"worried",
"anxious",
"nervous",
"confused",
"concerned",
"frantic",
"terrified",
"awed",
"astonished",
"afraid",
"startled",
"surprised",
"apprehensive",
"unsure",
"interested",
"intrigued",
"mesmerized",
"amazed",
"fixated",
"obsessed",
"exuberant",
"thrilled",
"excited",
"enthusiastic",
"giddy",
"jolly",
"happy",
"satisfied",
"overjoyed",
"content",
"calm",
"sad",
"grief",
"depressed",
"despair",
"distraught",
"dissapointed",
"hurt"
]

words = dict()

for e in emotion:
	words[e] = dict()
	# w = wn.synsets(e)
	reverse = wordsApi.reverseDictionary(e)
	rel = wordApi.getRelatedWords(e)
	# print w
	# if reverse.results is not None:
	# 	for related in reverse.results:
	# 		if not words[e].has_key(related.word):
	# 			words[e][related.word] = dict()
	if rel is not None:
		for r in rel:     
			if r.relationshipType != "antonym" and r.relationshipType != "hypernym" and  r.relationshipType != "rhyme" and  r.relationshipType != "same-context":
				for w in r.words:
					w = w.encode("utf-8")           
					if not words[e].has_key(w):
						words[e][w] = dict() 

for e in emotion:
	if words.has_key(e):
		for s in words[e]:
			# w = wn.synsets(s)
			reverse = wordsApi.reverseDictionary(e)
			rel = wordApi.getRelatedWords(e)
			# if reverse.results is not None:
			# 	for related in reverse.results:
			# 		if not words[e][s].has_key(related.word):
			# 			words[e][s][related.word] = dict()
			if rel is not None:
				for r in rel:     
					if r.relationshipType != "antonym" and r.relationshipType != "hypernym" and  r.relationshipType != "rhyme" and  r.relationshipType != "same-context":
								for w in r.words:
									w = w.encode("utf-8")           
									if not words[e].has_key(w):
										words[e][s][w] = dict() 

save_obj(words, "obj/rel_words2" )
