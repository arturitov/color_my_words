
from PIL import Image
from random import randint
from colour import Color
import time
import sys
import words
import sentiment


def createSplash(color,size,og_file):

	# img = Image.open('img/splatters.jpg')
	img = Image.open(og_file)
	img = img.convert("RGBA")
	pixdata = img.load()

	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
	        if pixdata[x, y][3] <= 255 and pixdata[x, y][3] > 0:
	            pixdata[x, y] = color
	
	img = img.resize(size, Image.ANTIALIAS)
	return img

# def splashesLayer(color,size):
# 	img = Image.open('img/splatters.jpg')
# 	img = img.convert("RGBA")
# 	pixdata = img.load()

# 	for y in xrange(img.size[1]):
# 	    for x in xrange(img.size[0]):
# 	        if pixdata[x, y][3] <= 255 and pixdata[x, y][3] > 0:
# 	            pixdata[x, y] = color
# 	img = img.resize(size, Image.ANTIALIAS)
# 	return img


def splashLayer(emotion_list,frequency,weight_dimensions,background,colors):
	for emotion in reversed(emotion_list):
		#Create a splash of the emotions color to the size/amount of its weight.
		emotion_weight = frequency[emotion]['weight']
		size = weight_dimensions[emotion_weight]
		# print size
		color = Color(colors[emotion]).rgb
		r = int(255 * color[0])
		g = int(255 * color[1])
		b = int(255 * color[2])
		rgb = (r,g,b)

		files = ['img/splatter.png','img/splatter2.png','img/splatter3.png']

		# for og_file in files:
		# print randint(0,len(files))
		og_file = files[randint(0,0)]
		img = createSplash(rgb,size,og_file)
		rotate = 0
		if randint(0,1):
			rotate = 180
		img = img.rotate(rotate)
		off_x = (randint(-(size[0]/2) ,background.size[0]-(size[0]/2)))
		off_y = (randint(-(size[1]/2) ,background.size[1]-(size[1]/2)))
		background.paste(img, ( off_x , off_y),mask=img)

	return background

def main():

	top_hit, frequency, emotion_list = words.map_words()

	colors = {
		"bored" : "#F4CAF4",
		"distracted" : "#DFC9F0",
		"disbelief" : "#D978D4",
		"distate" : "#A473CB",
		"disgusted" : "#7539AE",
		"disdain" : "#4F1E7E",
		"apathetic" : "#A01F60",
		"irate" : "#EA2207",
		"angry" : "#FF2807",
		"loathing" : "#401665",
		"bitter" : "#7C2102",
		"enraged" : "#7C2102",
		"contemptuous" : "#931632",
		"irritated" : "#F15A82",
		"cranky" : "#EEA7BC",
		"aggravated" : "#FEA7A5",
		"upset" : "#FF997E",
		"frustrated" : "#FF7D33",
		"hysterical" : "#000000",
		"frantic" : "#7B4B06",
		"worried" : "#E79918",
		"anxious" : "#FFA032",
		"nervous" : "#FFC582",
		"confused" : "#FFDFAE",
		"concerned" : "#FFC55A",
		"frantic" : "#7B5107",
		"terrified" : "#A48D16",
		"awed" : "#CFB01E",
		"astonished" :"#CEC61F",
		"afraid" : "#FFE13A",
		"startled" : "#FFD55D",
		"surprised" : "#FFDF83",
		"apprehensive" : "#FFEC84",
		"unsure" : "#FFFDD4",
		"interested" : "#E1EC7C",
		"intrigued" : "#CBE139",
		"mesmerized" : "#C3DD24",
		"amazed" : "#ACC61E",
		"fixated" : "#9AB01A",
		"obsessed" : "#285609",
		"exuberant" : "#31710E",
		"thrilled" : "#3C8E13",
		"excited" : "#42A017",
		"enthusiastic" : "#45B41A",
		"giddy" : "#7EC74B",
		"jolly" : "#9EDBA1",
		"happy" : "#27B42E",
		"satisfied" : "#6AD170",
		"overjoyed" : "#00B268",
		"content" : "#C7F1E2",
		"calm" : "#C9EFF3",
		"sad" : "#0378BB",
		"grief" : "#0072A4",
		"depressed" : "#004273",
		"despair" : "#181050",
		"distraught" : "#002B96",
		"dissapointed" : "#91A0E3",
		"hurt" : "#C2D6EF"
}


	max_weight = frequency[top_hit]['weight']
	weight_list = reversed(range(1,max_weight+1))

	weight_dimensions = {}

	for weight in weight_list:

		if int(weight) == max_weight:
			weight_dimensions[weight] = (2000,1400)
			weight_dimensions[weight] = (1400,960)
		else:
			x = int(weight_dimensions[weight+1][0] * .75)
			y = int(weight_dimensions[weight+1][1] * .75)
			if x < 400:
				x = 442
			if y < 300:
				y = 303
			weight_dimensions[weight] = (x,y)

	n = sentiment.background_color()
	background = Image.new('RGBA', (2000,1000), (n, n, n, 255))
	# background2 = Image.new('RGBA', (2000,1500), (0, 0, 0, 0))
	background = splashLayer(emotion_list,frequency,weight_dimensions,background,colors)
	background = splashLayer(emotion_list,frequency,weight_dimensions,background,colors)
	
	background.show()
	background.save("img/tweet.png")


if __name__ == '__main__':   
     main()
# 