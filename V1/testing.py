from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
##############################################################
PATH = "C:\chromedriver.exe"


print("1. One Way\n2. Round Trip\n3. Multi City")
trip = int(input("select the trip option: "))
print()
print('1. Economy Class\n2. Premium Economy Class\n3. Business Class\n4. First Class')
Class = int(input('Enter The Class You Would Like To Fly In : '))
print()
print()
print('MAX Number Of People is 9')
print('You Must Have 1 Adult for 2 Infant')
print('You Can Have Up To 8 Children, BUT There Must Be At Lest ONE Adult')
print('For Each Infant on Lap There Must Be One Adult')
print()

while True:
    People_count = 0
    adults = int(input('Enter number of Adult : '))
    People_count += adults
    if People_count > 9:
        print("Error: You Can't Have More Then ")
        continue

    child = int(input('Enter number of Child/Children : '))
    People_count += child
    if People_count > 9:
        print("Error: You Can't Have More Then ")
        continue

    infant_seat = int(input('Enter number of Infant : '))
    People_count += infant_seat
    if People_count > 9:
        print("Error: You Can't Have More Then ")
        continue

    infant_lap = int(input('Enter number of Ultra Smol BLACK NIGGER : '))
    People_count += infant_lap
    if People_count > 9:
        print("Error: You Can't Have More Then ")
        continue
    else:
        break



flag_1=True

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/travel/flights')
time.sleep(2)


if trip>3:
    print("wrong input, please input the correct option number")
    flag_1=False

if flag_1==True:
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]")
    time.sleep(0.5)
    ActionChains(driver).click(a).perform()

    if trip == 1:  # One Way
        b = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]")
        time.sleep(0.5)
        ActionChains(driver).click(b).perform()
    elif trip == 2:  # Round trip
        c = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[1]")
        time.sleep(0.5)
        ActionChains(driver).click(c).perform()
    elif trip == 3:  # Multi City
        d = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[3]")
        time.sleep(0.5)
        ActionChains(driver).click(d).perform()

    if flag_1:
        if trip==1:  # One Way
            # From city
            a = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input")
            a.clear()
            a.send_keys("GOI")
            time.sleep(1)
            a = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]")
            ActionChains(driver).click(a).perform()

            # To city
            a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input")
            a.clear()
            a.send_keys("KWI")
            time.sleep(1)
            a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]")
            ActionChains(driver).click(a).perform()
            time.sleep(1)

            # Date
            a = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            ActionChains(driver).click(a).perform()
            a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input")
            time.sleep(0.5)
            a.send_keys(Keys.BACKSPACE)
            a.send_keys("27/7/2023")
            time.sleep(0.5)

            # Date done button
            a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button")
            ActionChains(driver).click(a).perform()
            time.sleep(0.5)



        elif trip==2:  # Round Trip
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
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
            ActionChains(driver).click(a).perform()


            # Date From
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            ActionChains(driver).click(a).perform()
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input")
            time.sleep(0.5)
            a.send_keys(Keys.BACKSPACE)
            a.send_keys("27/7/2023")
            time.sleep(0.5)


            # Date To
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input")
            time.sleep(0.2)
            for i in range(11):
                a.send_keys(Keys.BACKSPACE)
            a.send_keys("30/7/2023")
            time.sleep(0.5)

            # Date done button
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button")
            ActionChains(driver).click(a).perform()
            time.sleep(0.5)

        elif trip == 3:
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys("GOI")
            time.sleep(1)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li[1]''')
            ActionChains(driver).click(a).perform()

            time.sleep(1)

            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys("GOI")
            time.sleep(1)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li''')
            ActionChains(driver).click(a).perform()

            time.sleep(1)

            # Check X-Path Again


            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys("GOI")
            time.sleep(1)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li''')
            ActionChains(driver).click(a).perform()









# Number of people



a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/button")
ActionChains(driver).click(a).perform()
time.sleep(0.5)

for i in range(adults-1):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[1]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(0.1)

for i in range(child):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[2]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(0.1)

for i in range(infant_seat):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[3]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(0.1)

for i in range(infant_lap):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[4]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(0.1)

a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/button[1]")
ActionChains(driver).click(a).perform()
time.sleep(0.5)



# Type of Class
a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[1]")
ActionChains(driver).click(a).perform()
time.sleep(0.5)
if Class == 2:
    a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[2]")
    ActionChains(driver).click(a).perform()
    time.sleep(0.5)

elif Class == 3:
    a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[3]")
    ActionChains(driver).click(a).perform()
    time.sleep(0.5)

elif Class == 4:
    a = driver.find_element(By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[4]")
    ActionChains(driver).click(a).perform()
    time.sleep(0.5)





# Search
a = driver.find_element(By.XPATH,
                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button''')
ActionChains(driver).click(a).perform()
time.sleep(2)

