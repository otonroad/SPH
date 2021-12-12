# /bin/env python3 python3 main.py

# Author: otonroad
# Date: Dec. 2020
# Version: 1.0
# License: MIT

# this is the main file of the project

# Importing the libraries
from translate import Translator, translate
import os
import requests
from selenium import webdriver
from time import sleep

def get_html_snapshot(name):
    # this sends a request to the website and returns the html code
    # to see if the website is up and running
    try:
        filename = name + ".html"; file = open(filename, "w")
        url = "https://www.google.com/"; data = requests.get(url).text
        file.write(data); file.close()
        return filename
    except:
        return None

def get_html_snapshot_selenium(name):
    # this sends a request to the website and returns the html code
    # to see if the website is up and running
    # file = open name + ".png", 'wb'); file.close();
    d = webdriver.Chrome(); d.get("https://www.google.com/search?q=" + name)
    sleep(0.5)
    d.find_element_by_id("L2AGLb").click()
    filename = "screenshot.png"; d.get_screenshot_as_file(filename); d.quit()

def getFile():
    f = open("spanishwords.txt", "r")
    lines = f.readlines()
    translator = Translator(from_lang="es", to_lang="en")
    for line in lines:
        print(line)
        get_html_snapshot_selenium(line)
        print("word meaning: " + translator.translate(line))

try:
    while True:
        getFile()
except KeyboardInterrupt:
    print("stopped ........")