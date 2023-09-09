from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#PATH = "C:\chromedriver.exe"
# flag_1 = True

u_from = "dxb"
u_dest = "cdg"
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
x=2
driver.get('https://www.flightradar24.com/')
#clicking continue with cookies button
driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/div/div/button').click()
time.sleep(x)

#search bar
a = driver.find_element(By.XPATH,'//*[@id="searchBox"]').click()
time.sleep(x)
#click flight by route opt
a = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
time.sleep(x)
#departure
a = driver.find_element(By.XPATH,'//*[@id="flight_by_route_from"]').click()
time.sleep(x)
a.send_keys(u_from)
time.sleep(x)
a = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/ul/li[1]/a/span[1]').click()
#arrival
a = driver.find_element(By.XPATH,'//*[@id="flight_by_route_to"]').click()
a.send_keys(u_dest)
time.sleep(x)
a = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li/a/span[1]').click()

time.sleep(100)