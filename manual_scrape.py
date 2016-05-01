import bs4
import requests
import sys
import qoutes_emotions2 as qoutes
import tinyurl
import time
import tweet, tweet_lyrics
import save_load_obj as slo
from random import randint

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
    print url
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

def main(text,url,title):

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


if __name__ == '__main__':   
    text = sys.argv[1]
    url = sys.argv[2]
    title = sys.argv[3]
    main(text,url,title)