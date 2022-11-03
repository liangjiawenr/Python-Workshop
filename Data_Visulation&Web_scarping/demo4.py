# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:12:48 2022

@author: 2244530j
Only for PhD Python Workshop, Univeristy of Glasgow.
"""

#pip install requests
#import
import requests
import re
import os
#Step 1: Scrape the whole page
#request headers
headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
#url for the website
url = 'https://www.bbc.co.uk/news/technology-63483695'
#request and response
page_text = requests.get(url=url,headers=headers).text

#Step 2: Request all pictures
pic = '<picture>.*?src="(.*?)" width.*?</picture>'

pic_src_list = re.findall(pic, page_text, re.S)

print(pic_src_list)

#Step 3: save all pictures in the list
#create a folder
if not os.path.exists('./pics'):
    os.mkdir('./pics')
#save
for i in pic_src_list:
    #request binary contents for the pictures
    image_b = requests.get(url = i,headers = headers).content
    #name the pictures
    image_name = i.split('/')[-1]
    #saving path
    image_path = './pictures/' + image_name
    #save
    with open(image_path, 'wb') as fp:
        fp.write(image_b)
    #success
    print(image_name,'successfully downloaded')    
    