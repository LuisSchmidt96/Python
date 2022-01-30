import json
import pandas as pd
import requests
import urllib.request
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


#initiate data storage

titles = []
links = []
titlelist = []
linklist = []
chapterlist = []
offset = 0

#scraping titles
for i in range(20):
    url = "https://www.wattpad.com/v4/search/stories?query=%23niallhoran&fields=stories(id%2Ctitle%2CvoteCount%2CreadCount%2CcommentCount%2Cdescription%2Ccompleted%2Cmature%2Ccover%2Curl%2CisPaywalled%2Clength%2Clanguage(id)%2Cuser(name)%2CnumParts%2ClastPublishedPart(createDate)%2Cpromoted%2Csponsor(name%2Cavatar)%2Ctags%2Ctracking(clickUrl%2CimpressionUrl%2CthirdParty(impressionUrls%2CclickUrls))%2Ccontest(endDate%2CctaLabel%2CctaURL))%2Ctotal%2Ctags%2Cnexturl&limit=100&minParts=60&mature=true&offset="+str(offset)
    results = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(results)
    data = results.json()['stories']
    for j in range(len(data)):
        try:
            name = data[j]['title']
            chapters = data[j]['numParts']
            if (name[0]==('H' or 'h') and (65 <= chapters <= 72)):    
                print(name+"   "+str(chapters))
                titlelist.append(name)
                linklist.append(data[j]['url'])
                chapterlist.append(chapters)
        except:
            break
    print('Page: '+str(i)+' Offset: '+str(offset))
    offset = offset + len(data)

  
endlist = {'Titel': titlelist, 'Kapitel': chapterlist, 'Link': linklist}    
table = pd.DataFrame(endlist)
table.to_csv('table_api.csv')
