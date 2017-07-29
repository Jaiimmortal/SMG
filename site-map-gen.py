
# coding: utf-8

# In[33]:

import requests
from bs4 import BeautifulSoup
import pandas as pd

def calculateinternallink(url, includeUrl, tobeAdded):
    return url.split('/')[0] + '//' + includeUrl + tobeAdded

def splitaddress(url):
    includeUrl = url.split('/')[2]
    return includeUrl

def findall_internal_links(url, internalLinks):
    
    final_list_internal_links = []
    includeUrl = splitaddress(url)
    
    for each_internal_link in internalLinks:
        proper_internal_link = calculateinternallink(url, includeUrl, each_internal_link)
        final_list_internal_links.append(proper_internal_link)
        
    return final_list_internal_links

def newUrl2scrape(final_list):
    
    for newLinktoscrape in final_list:
        if newLinktoscrape not in pages:
            #print(newLinktoscrape)
            return newLinktoscrape
        continue
    

def spider(max_pages):
    count = 1
    url = 'http://biosql.org/wiki/Main_Page'
    while count <= max_pages:
        
        internalLinks, internalLinkstitle, externalLinks, externalLinkstitle = [], [], [], []
        html_page = requests.get(url).text
        soup = BeautifulSoup(html_page, 'lxml')
        
        for link in soup.findAll('a'):
            if link.attrs['href'] is not None:
                href = link.get('href')
                link_title = link.string

                if href.startswith('/'):
                    internalLinks.append(href)
                    internalLinkstitle.append(link_title)
                   
                elif href.startswith(('https', 'http', 'www')):
                    externalLinks.append(href)
                    externalLinkstitle.append(link_title)
                    
                else:
                    pass
        
        pages.add(url)
        
        count += 1
                
        print(internalLinks)
        print(externalLinks)
        
        final_list = findall_internal_links(url, internalLinks)
        print(url, '\n\n---------')
        print(pd.DataFrame({'Link':internalLinks, 'Title':internalLinkstitle}))
        print(pd.DataFrame({'Link':externalLinks, 'Title':externalLinkstitle}))
        url = newUrl2scrape(final_list)
        
#         global IL, EL
#         IL = pd.DataFrame({'Link':internalLinks, 'Title':internalLinkstitle})
#         EL = pd.DataFrame({'Link':externalLinks, 'Title':externalLinkstitle})

        

pages = set()
spider(6)

print(pages)

