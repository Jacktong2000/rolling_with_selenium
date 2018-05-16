#! usr/bin/env python3

from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import os
from pyvirtualdisplay import Display

#define webdriver and webdriver path
driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")

#site to open

def google():
    driver.get('http://google.com');

    #time.sleep(2);

    search_box= driver.find_element_by_name('q')
    search_box.send_keys('John Oliver')
    search_box.submit()

    #Finds link on Google search results
    links = []
    search_result = driver.find_elements_by_class_name('r');
    for i in search_result:
        #print(i.find_element_by_css_selector('a').get_attribute('href'))
        links.append(i.find_element_by_css_selector('a'))

    links[4].click()
    time.sleep(2)

    driver.quit()

google()

def cnn_img():
    driver.get('http://cnn.com');

    search_result = driver.find_elements_by_css_selector('img')
    for i in search_result:
        print (i.get_attribute('src'))
    driver.quit()

def cnn_headline(keyword):
    driver.get('http://cnn.com');

    search_result = driver.find_elements_by_class_name('cd__headline-text')
    for i in search_result:
        if keyword.lower() in i.text.lower():
            print(i.text)
    #print (search_result.text)
    driver.quit()

#cnn_headline(input('Enter keyword: '))
