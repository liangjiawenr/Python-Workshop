# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:26:00 2022

@author: 2244530j
Only for PhD Python Workshop, Univeristy of Glasgow.
"""

"""
Objective: download and save a picture
"""

#pip install requests
#import
import requests

#Step 1: Target
#url for the picture
url = 'https://ichef.bbci.co.uk/onesport/cps/976/cpsprodpb/2FBA/production/_127481221_engsco.jpg'
#request headers
headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

#Step 2: request the url
response = requests.get(url = url)

#Step 3: obtain the response
#text: strings; content: binary; 
image = response.content

#Step 4: save
with open('./image.jpg', 'wb') as fp:
    fp.write(image)
    
    