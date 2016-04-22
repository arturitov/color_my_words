
from PIL import Image
from random import randint
from random import uniform
from random import shuffle
from colour import Color
import save_load_obj as slo
import time
import sys
import os



def createSplash(color,og_file):

	# img = Image.open('img/splatters.jpg')
	img = Image.open(og_file)
	# img.show()
	img = img.convert("RGBA")
	pixdata = img.load()

	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
	    	if pixdata[x, y][1] > 200:
	    		pixdata[x,y] = (0,0,0,0)
	        if pixdata[x, y][3] <= 255 and pixdata[x, y][3] > 0:
	        	# print pixdata[x, y], color
	    		pixdata[x, y] = color

	# img.show()
	if og_file == 'img/splatter2.png' or og_file == 'img/splatter3.png':
		ran = uniform(1.0, 1.5)
		img = img.resize((int(img.size[0]*ran),int(img.size[1]*ran)), Image.ANTIALIAS)
	elif og_file.startswith('img/fear'):
		ran = uniform(1.5, 2.5)
		img = img.resize((int(img.size[0]*ran),int(img.size[1]*ran)), Image.ANTIALIAS)
	elif og_file.endswith('img/splatter.png'):
		ran = uniform(0.2, 1.0)
		img = img.resize((int(img.size[0]*ran),int(img.size[1]*ran)), Image.ANTIALIAS)
	else:
		ran = uniform(0.8, 1.2)
		img = img.resize((int(img.size[0]*ran),int(img.size[1]*ran)), Image.ANTIALIAS)
	return img

def get_colors(og_file,colors,emotion):
	img = Image.open(og_file)
	img = img.convert("RGBA")
	pixdata = img.load()
	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
	        colors[emotion].append(pixdata[x, y])

	
def splashLayer(emotion,background,colors):
	ran = list()
	if len(emotion) < 2:
		x = 30
	else:
		x = 20
	for e in emotion:
		for i in xrange(0,x):
			ran.append(colors[e][randint(0,len(colors[e])-1)])
		x = x / 2
	shuffle(ran)
	# for e in emotion:
	# 	# for x in xrange(0,x):
	# 	# 	ran.append(colors[e][randint(0,len(colors[e])-1)])
	c = 0
	for i in ran:
		print c
		c += 1
		path = 'img/splatter/'
		files = list()
		for j in os.listdir(path):
				if j.endswith('.png'):
					files.append(path+j)
					img = Image.open(path+j)
		# files = ['img/splatter.png','img/splatter3.png','img/splatter.png','img/splatter.png']
		og_file = files[randint(0,len(files)-1)]
		# og_file = files[3]
		size = (1400,960)
		img = createSplash(i,og_file)
		rotate = 0
		if randint(0,1):
			rotate =180
		img = img.rotate(rotate)
		off_x = (randint(-(img.size[0]/2) ,background.size[0]-(img.size[0]/2)))
		off_y = (randint(-(img.size[1]/2) ,background.size[1]-(img.size[1]/2)))
		# off_x = randint(0,background.size[0])
		# off_y = randint(0,background.size[1])
		background.paste(img, ( off_x , off_y),mask=img)
	x = x / 2
	try:
		for x in xrange(0,4):
			if randint(0,1):
				print x
				path = "img/"+emotion[0]+'/'
				images = list()
				for i in os.listdir(path):
					if i.endswith('.png'):
						images.append(path+i)
				image = images[randint(0,len(images)-1)]
				if randint(0,1):
					img = createSplash((0,0,0,250),image)
				else:
					img = createSplash((250,250,250,250),image)
				# if randint(0,1):
				# 	rotate = 45
				# 	img = img.rotate(rotate)
				try:
					off_x = (randint(-(img.size[0]/4) ,background.size[0]-(img.size[0]/4)))
					off_y = (randint(-(img.size[0]/4) ,background.size[1]-(img.size[1]/4)))
					background.paste(img, ( off_x , off_y),mask=img)
				except Exception, e:
					print e
	except Exception, e:
		print e


	return background


def main(emotion_list):
	# emotion_list = get_emotion.main()
	# emotion_list = ['joy']
	colors = dict()
	colors['anger'] = list()
	colors['joy'] = list()
	colors['sadness'] = list()
	colors['disgust'] = list()
	colors['fear'] = list()

	for e in colors:
		for i in os.listdir("img/emotions/"+e):
			if i.endswith('.png'):
				get_colors("./img/emotions/"+e+"/"+i,colors,e)

	slo.save_obj(colors,"obj/colors")
	# colors = slo.load_obj("obj/colors")

	# for c in colors:
	# 	print c, len(colors[c])

	# n = sentiment.background_color()
	# background = Image.new('RGBA', (2000,1000), (n, n, n, 255))
	if emotion_list[0] == 'joy':
		background = Image.new('RGBA', (1800,1350), (255, 255, 255, 255))
	else:
		background = Image.new('RGBA', (1800,1350), (0, 0, 0, 255))

	print "Finding Image...\n"
	background = splashLayer(emotion_list,background,colors)
	# background.show()
	# 
	# background = splashLayer(['joy', 'fear'],background,colors)
	# background.show()

	background.save("img/tweet.png")


if __name__ == '__main__':   
     main(emotion_list)
# 
