from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# PATH = "C:\chromedriver.exe"
# flag_1 = True

u_from = "dxb"
u_dest = "cdg"
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.flightradar24.com/')
# clicking continue with cookies button
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/div/div/button').click()
time.sleep(2)

# search bar
driver.find_element(By.XPATH, '//*[@id="searchBox"]').click()
time.sleep(2)

# click flight by route opt
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
time.sleep(2)

# departure
driver.find_element(By.XPATH, '//*[@id="flight_by_route_from"]').send_keys(u_from)
time.sleep(2)

# arrival
driver.find_element(By.XPATH, '//*[@id="flight_by_route_to"]').send_keys(u_dest)
time.sleep(2)

# search
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/button').click()
time.sleep(100)