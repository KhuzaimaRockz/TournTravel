from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
##############################################################
PATH = "C:\chromedriver.exe"
print("1. 1 way\n2. 2 way\n3. multicity")
trip = int(input("select the trip option: "))
flag_1=True

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/travel/flights')
time.sleep(3)

a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]")
ActionChains(driver).click(a).perform()

if trip==1:
    b=driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]")
    ActionChains(driver).click(b).perform()
elif trip==2:
    c=driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[1]")
    ActionChains(driver).click(c).perform()
elif trip==3:
    d=driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[3]")
    ActionChains(driver).click(d).perform()
else:
    print("wrong input, please input the correct option number")
    flag_1=False

if flag_1==True:
    if trip==1:
        a = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input")
        a.clear()
        a.send_keys("GOI")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]")
        ActionChains(driver).click(a).perform()

        a.send_keys("KWI")
        a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input")
        a.clear()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]")
        ActionChains(driver).click(a).perform()
    elif trip==2:
        a = driver.find_element(By.XPATH,
                                '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input''')
        a.clear()
        a.send_keys("GOI")
        time.sleep(1)
        a = driver.find_element(By.XPATH,
                                '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
        ActionChains(driver).click(a).perform()

        a = driver.find_element(By.XPATH,
                                '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input''')
        a.clear()
        a.send_keys("KWI")
        time.sleep(1)

        a = driver.find_element(By.XPATH,
                                '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li''')
        ActionChains(driver).click(a).perform()

        time.sleep(1)