# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:14:35 2022

@author: 2244530j
Only for PhD Python Workshop, Univeristy of Glasgow.
"""

"""
Objective: download and save a google search result web page
"""

#pip install requests
#import
import requests

#Step 1: Web Targeting
#request headers
headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
#url = 'https://www.google.co.uk/search?q=test'
url = 'https://www.google.co.uk/search'
#the parameters of the url
search = input('enter what to search:')
param ={
        'query': search
        }

#Step 2: Request url with parameters
response = requests.get(url = url, params = param, headers = headers)

#Step 3: Obtain and Parse the Response
page_text = response.text

#Step 4: Data Saving 
fileName = search + '.html'
with open(fileName, 'w', encoding = 'utf-8') as fp:
    fp.write(page_text)

#Finish
    print(fileName, 'is successfully downloaded')
    
    
    
