# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:12:48 2022

@author: 2244530j
Only for PhD Python Workshop, Univeristy of Glasgow.
"""

#pip install selenium
#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import request
import requests
import re

#1.get all texts for the links
url ='https://www.gla.ac.uk/schools/business/staff/#research%26teaching'
page_text = requests.get(url).text
staff = '</strong>.*? (.*?)</a>'
staff_list = re.findall(staff,page_text,re.S)
print(staff_list)

#2.launch the driver
driver = webdriver.Chrome(executable_path= 'C:/Users/Jiang/Downloads/chromedriver_win32/chromedriver')
driver.get(url=url)
driver.maximize_window()
#3.interaction
for i in staff_list[0:2]:
    driver.find_element(By.PARTIAL_LINK_TEXT,i).click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

#please finish the codes by yourselves

#quit
driver.quit()

