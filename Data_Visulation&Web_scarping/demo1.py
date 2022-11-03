# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:00:02 2022

@author: Z jiang
Only for PhD Python Workshop, Univeristy of Glasgow.
"""


"""
Objective: download a web page and save
"""

#pip install requests
#import
import requests

#Step 1: Web Targeting
url = 'https://www.bbc.co.uk/sport/football/63469211'
  
#Step 2: Request
response = requests.get(url = url)
  
response = requests.get('https://www.bbc.co.uk/sport/football/63469211')

#Step 3: Obtain the Response
page_text = response.text
  
print(response)
  
print(page_text)

#Step 4: Data Saving 
with open('./web.html', 'w') as fp:
    fp.write(page_text)

#Finish
    print('successfully downloaded')

