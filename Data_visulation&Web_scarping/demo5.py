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
#launch the browser in selenium webdriver
driver = webdriver.Chrome(executable_path= 'C:/Users/Jiang/Downloads/chromedriver_win32/chromedriver')

#1. get the url
driver.get('https://scholar.google.com/')

#2. send keys
#find the position of the search bar
element = driver.find_element(By.ID,'gs_hdr_tsi')
#interact
keys = input('paper to search:')
element.send_keys(keys)

#3.search
#find the search button
btn = driver.find_element(By.ID,'gs_hdr_tsb')
#interact
btn.click()

#stop driver
driver.quit()
