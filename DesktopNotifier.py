import requests

import xml.etree.ElementTree as ET

RSS_FEED_URL = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"  

def loadRSS():
    resp = requests.get(RSS_FEED_URL)
    return(resp.content)

def parseXML(rss):
    root = ET.fromstring(rss)

    newsItems=[]

    for item in root.findall("./channel/item"):
        news={}
        for child in item:
            print("**child.tag:",child.tag)
            if child.tag=='{http://search.yahoo.com/mrss/}content url':
                news['media']=child.attrib['url']
            else:
                news[child.tag]=child.text
        newsItems.append(news)
    return newsItems

def topStories():
    rss = loadRSS()
    newsItems = parseXML(rss)
    return newsItems

