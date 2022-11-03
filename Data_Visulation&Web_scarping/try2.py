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
#launch the browser in selenium webdriver
driver = webdriver.Chrome(executable_path= 'C:/Users/Jiang/Downloads/chromedriver_win32/chromedriver')

#1. get the url
driver.get('https://www.gla.ac.uk/StudentPortal')

#2. positions
#find the position of username input
element1 = driver.find_element(By.ID,'username')
#find the position of password input
element2 = driver.find_element(By.ID,'password')

#3. interact
#interaction input
element1.send_keys('')
time.sleep(3)
element2.send_keys('')
time.sleep(3)
#interaction login
btn = driver.find_element(By.NAME,'_eventId_proceed')
btn.click()

#quit
driver.quit()
