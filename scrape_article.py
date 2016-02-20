import bs4
import requests
import sys
import qoutes_emotions2 as qoutes
import tinyurl
import time
import tweet
import save_load_obj as slo
from random import randint

def get_urls():

    # Extracts data from BBC news
    url  = "http://www.bbc.com/news"
    r = requests.get(url) 
    soup = bs4.BeautifulSoup(r.text,"html.parser") 
    html = ""

    # There are two section in the website that give the top news at that time
    url3 = soup.find('div',{"id":"comp-top-stories-3"}).find('div',{"class":"macaw"})
    url2 = soup.find('div',{"id":"comp-top-stories-2"})

    urls = []
    titles = []

    # Finds links for top new stories in those sections
    print "\n\nTop news article links found:"
    for a in url2.find_all('a', {"class":"faux-block-link__overlay-link"}):
        if a['href'] not in urls :
            print a['href']
            urls.append(a['href'])
    for a in url3.find_all('a', {"class":"title-link"}):
        if a['href'] not in urls :
            print a['href']
            urls.append(a['href'])

    print
    # this will get the tags that we are late
    title2 = soup.find('div',{"id":"comp-top-stories-2"}).find_all('span', {"class":"title-link__title-text"})
    title3 = soup.find('div',{"id":"comp-top-stories-3"}).find('div',{"class":"macaw"}).find_all('span', {"class":"title-link__title-text"})

    # Finds the title of the article
    for u2 in title2 :
        titles.append(u2.text)
    for u3 in title3:
        titles.append(u3.text)
        

    return urls, titles

def get_article_text(url):
    fo = open("txt/article.txt", "wb")
    r = requests.get(url) 
    soup = bs4.BeautifulSoup(r.text,"html.parser") 
    paragraphs = soup.find_all('p')
    text = " ".join([ paragraph.text.encode('utf-8') for paragraph in paragraphs])
    fo.write(text)
    fo.close()


def main():

    urls =[]
    titles = []
    urls, titles = get_urls()


    for x in xrange(0,len(urls)):
        url = urls[x]
        title = titles[x]

        if url[0] == "/":
            url = "http://www.bbc.com" + url
        try:
            visited = slo.load_obj("obj/visited")
        except:
            visited = {}
        if not visited.has_key(url):
            print visited
            visited[url] = True
            slo.save_obj(visited,"obj/visited")
            tiny = tinyurl.create_one(url)
            print "---------------------------------------------------"
            print tiny
            print url
            print "\n",title,"\n"

            # Outputs contents of article into txt/article.txt
            get_article_text(url)
            # Produces qoute based on the article
            success = tweet.main(tiny,title)

            print "---------------------------------------------------"
            # Produces a delay until the next tweet
            sleep_delay = randint(600,1800)
            if success:
                print "Delay",sleep_delay,"seconds"
                time.sleep(sleep_delay)

if __name__ == '__main__':   
     main()
