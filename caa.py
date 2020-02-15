# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:11:03 2020

@author: anusree
"""

import newspaper
from newspaper import Article
import nltk
import re


source = newspaper.build('https://www.thequint.com/' ,memoize_articles = False)
key = ['CAA', 'caa', 'nrc', 'NRC', 'Jamia', 'npr','NPR']
url=[]


for article in source.articles:
    
    #for downloading
    article.download()
    article.parse()
    article.nlp()
    a_key= article.keywords
    if(set(key).intersection(set(a_key))):
        url.append(article.url)
        
   #without downloading by using regex
    a_url = re.split(r'[/\-?]',article.url.lower())
    if(set(key).intersection(set(a_url))):
        url.append(article.url)
    
  
    
            


