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
url = 'https://www.gla.ac.uk/schools/business/staff/#research%26teaching'
#request and response
page_text = requests.get(url=url,headers=headers).text

#Step 2: Request all first names
staff = '<strong>(.*?)</strong>.*? (.*?)</a>'

staff_list = re.findall(staff, page_text, re.S)

print(staff_list)


#Step 3: save
#create a folder
if not os.path.exists('./STAFF'):
    os.mkdir('./STAFF')

#save
for i in staff_list[0:5]:
    #staff name
    staffName = i[0]+' '+i[1]
    #file name
    fileName = i[0]+' '+i[1]+'.txt'
    #saving path
    staff_path = './STAFF/' + fileName
    #save
    with open(staff_path, 'w') as fp:
        fp.write(staffName)
    #success
    print(fileName,'successfully downloaded')