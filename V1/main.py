from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
################

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome()



driver.get('https://www.google.com/travel/flights')
time.sleep(5)
a = driver.find_element(By.XPATH, '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input''')
a.clear()
a.send_keys("GOI")
time.sleep(1)
a = driver.find_element(By.XPATH, '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
ActionChains(driver).click(a).perform()



a = driver.find_element(By.XPATH, '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input''')
a.clear()
a.send_keys("KWI")
time.sleep(1)
a = driver.find_element(By.XPATH, '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li''')
ActionChains(driver).click(a).perform()

time.sleep(1)


a = driver.find_element(By.XPATH, '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button''')
ActionChains(driver).click(a).perform()








