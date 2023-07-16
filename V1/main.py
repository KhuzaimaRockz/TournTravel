from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import json
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import csv
from bs4 import BeautifulSoup
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
import tkinter.font as font
import datetime
import webbrowser
#########################################################################

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://www.google.com/maps')
time.sleep(15)
url = driver.current_url
c1 = url.rfind("!3d")
cod1=""

for i in range(c1 + 3, c1 + 13):
    cod1+=url[i]
print(cod1)

c2 = url.rfind("!4d")
cod2=""

for i in range(c2 + 3, c2 + 13):
    cod2+=url[i]
print(cod2)