import bs4
import requests
import sys
import qoutes_emotions2 as qoutes
import tinyurl
import time
import tweet, tweet_lyrics
import save_load_obj as slo
from random import randint

def get_urls(text):
    urls = []
    titles = []
    if text == "news":
        # Extracts data from BBC news
        url  = "http://www.bbc.com/news"
        r = requests.get(url) 
        soup = bs4.BeautifulSoup(r.text,"html.parser") 
        html = ""

        # There are two section in the website that give the top news at that time
        url3 = soup.find('div',{"id":"comp-top-stories-3"}).find('div',{"class":"macaw"})
        url2 = soup.find('div',{"id":"comp-top-stories-2"})

        # urls = []
        # titles = []

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
    elif text == "lyrics":
        url = "http://www.metrolyrics.com/top100.html"
        r = requests.get(url) 
        soup = bs4.BeautifulSoup(r.text,"html.parser") 
        html = ""
        top_20 = soup.find('ul',{"class":"top20"})
        for song in top_20.find_all('span',{"class":"song"}):
            for box in song.find_all('a'):
                try:
                    if box['href'] not in urls and box['href'].endswith('html') and "song-link" in box['class']:
                        urls.append(box['href'])
                        print "---------------------------"
                        print box['href']
                        for v in box:
                            title = str(v).strip()
                            print title
                except:
                    pass
            for artist in song.find_all('span',{"class":"artist"}):
                try:
                    # print vars(artist)
                    for a in artist:
                        for aa in a:
                            if len(aa) > 3:
                                arts = str(aa).strip().strip()
                                print arts 
                except:
                    pass
            title = arts + " - " + title
            title = title[:title.find("Lyrics")-1]
            titles.append(title)
    len(urls)
    return urls, titles

def get_article_text(url):
    fo = open("txt/article.txt", "wb")
    test = open("txt/article_test.txt", "wb")
    r = requests.get(url) 
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    try:
        article_body = soup.find('div',{'property':"articleBody"}) 
        paragraphs = article_body.find_all('p')
    except:
        article_body = soup.find('div',{'class':"main_content_wrapper"}) 
        paragraphs = article_body.find_all('p')
        # print pararaphs
    text = "\n".join([ paragraph.text.encode('utf-8') for paragraph in paragraphs])
    # print text
    text_test = " ".join([ paragraph.text.encode('utf-8') for paragraph in paragraphs])
    test.write(text_test)
    test.close()
    fo.write(text)
    fo.close()

def get_lyrics(url):
    fo = open("txt/lyrics.txt", "wb")
    r = requests.get(url) 
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    # print soup
    lyric_body = soup.find('div',{'id':"lyrics-body-text"})
    # print lyric_body
    paragraphs = lyric_body.find_all('p')
    # print "hi"
    # print paragraphs
    # print paragraphs
    text = "\n".join([ paragraph.text.encode('utf-8') for paragraph in paragraphs])
    # print text
    fo.write(text)
    fo.close()


def main(text):

    urls =[]
    titles = []
    # text = "lyrics" #["news","lyrics"]
    urls, titles = get_urls(text)


    for x in xrange(0,len(urls)):
        url = urls[x]
        title = titles[x]
        if text == "news":
            if url[0] == "/":
                url = "http://www.bbc.com" + url
        elif text == "lyrics":
            url = url
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
            if text == "news":
                get_article_text(url)
                success = tweet.main(tiny,title,text)
            elif text == "lyrics":
                get_lyrics(url)
                success = tweet_lyrics.main(tiny,title,text)
            # Produces qoute based on the article
            

            print "---------------------------------------------------"
            # Produces a delay until the next tweet
            sleep_delay = randint(600,1800)
            # sleep_delay = 5
            if success:
                print "Delay",sleep_delay,"seconds"
                time.sleep(sleep_delay)

if __name__ == '__main__':   
    text = sys.argv[1]
    main(text)
