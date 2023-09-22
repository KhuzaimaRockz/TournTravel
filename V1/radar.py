from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


#need to integrate this code to main.py
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.flightradar24.com/')
# clicking continue with cookies button
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(2)

# search bar
driver.find_element(By.XPATH, '//*[@id="searchBox"]').click()
time.sleep(2)

# click flight by route opt
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
time.sleep(2)

# departure
driver.find_element(By.XPATH, '//*[@id="flight_by_route_from"]').send_keys(usr_dest)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/ul/li/a/span[1]').click()
time.sleep(2)

# arrival
driver.find_element(By.XPATH, '//*[@id="flight_by_route_to"]').send_keys(u_dest)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li/a/span[1]').click()
time.sleep(2)

# search
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/button').click()
time.sleep(2)

#if live aircrafts are available
element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/h2')
search="LIVE FLIGHTS"
if search not in element.text:
    print("No Live Flights")
else:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/a').click()
    time.sleep(2)
    element=driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a[3]')
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a[1]/span').click()
time.sleep(100)