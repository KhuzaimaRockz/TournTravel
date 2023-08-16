from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

##############################################################
PATH = "C:\chromedriver.exe"
x = 2

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

    infant_lap = int(input('Enter number of Infant on lap : '))
    People_count += infant_lap
    if People_count > 9:
        print("Error: You Can't Have More Then ")
        continue
    else:
        break

if trip == 1:  # One Way
    usr_from = input('Enter -From- location : ')
    usr_dest = input('Enter -Destination- : ')
    date_from = input('Enter Date of flight (dd/mm/yyyy) :')

elif trip == 2:  # Round Trip
    usr_from = input('Enter -From- location : ')
    usr_dest = input('Enter -Destination- : ')
    date_from = input('Enter Date of First Flight (dd/mm/yyyy) :')
    date_to = input('Enter Date of Second Flight (dd/mm/yyyy) :')

elif trip == 3:
    flights = int(input('Enter Number of flights : '))
    usr_from = input('Enter -From- location : ')
    usr_dest_1 = input('Enter -Destination- 1 : ')
    date_from = input('Enter Date of First Flight (dd/mm/yyyy) :')

    if flights >= 2:
        usr_dest_2 = input('Enter -Destination- 2 : ')
        date_to_2 = input('Enter Date of Second Flight (dd/mm/yyyy) :')

    if flights >= 3:
        usr_dest_3 = input('Enter -Destination- 3 : ')
        date_to_3 = input('Enter Date of Third Flight (dd/mm/yyyy) :')

    if flights >= 4:
        usr_dest_4 = input('Enter -Destination- 4 : ')
        date_to_4 = input('Enter Date of Fourth Flight (dd/mm/yyyy) :')

    if flights >= 5:
        usr_dest_5 = input('Enter -Destination- 5 : ')
        date_to_5 = input('Enter Date of Final Flight (dd/mm/yyyy) :')


flag_1 = True

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/travel/flights')
time.sleep(x)

if trip > 3:
    print("wrong input, please input the correct option number")
    flag_1 = False

if flag_1:
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]")
    time.sleep(x)
    ActionChains(driver).click(a).perform()

    if trip == 1:  # One Way
        b = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]")
        time.sleep(x)
        ActionChains(driver).click(b).perform()
    elif trip == 2:  # Round trip
        c = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[1]")
        time.sleep(x)
        ActionChains(driver).click(c).perform()
    elif trip == 3:  # Multi City
        d = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[3]")
        time.sleep(x)
        ActionChains(driver).click(d).perform()

    if flag_1:
        if trip == 1:  # One Way
            # From city
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input")
            a.clear()
            a.send_keys(usr_from)
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]")
            ActionChains(driver).click(a).perform()

            # To city
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input")
            a.clear()
            a.send_keys(usr_dest)
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]")
            ActionChains(driver).click(a).perform()
            time.sleep(x)

            # Date
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            ActionChains(driver).click(a).perform()
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input")
            time.sleep(x)
            a.send_keys(Keys.BACKSPACE)
            a.send_keys(date_from)
            a.send_keys(Keys.ENTER)
            time.sleep(x)



        elif trip == 2:  # Round Trip
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys(usr_from)
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
            ActionChains(driver).click(a).perform()

            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys(usr_dest)
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
            ActionChains(driver).click(a).perform()

            # Date From
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            ActionChains(driver).click(a).perform()
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input")
            time.sleep(x)
            a.send_keys(Keys.BACKSPACE)
            a.send_keys(date_from)
            time.sleep(x)

            # Date To
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input")
            time.sleep(x)
            for i in range(11):
                a.send_keys(Keys.BACKSPACE)
            a.send_keys(date_to)
            a.send_keys(Keys.ENTER)
            time.sleep(x)


        elif trip == 3:
            # Add Flight
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/button''')
            for i in range(flights - 2):
                ActionChains(driver).click(a).perform()
                time.sleep(x)

            # From City
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys(usr_from)
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li[1]''')
            ActionChains(driver).click(a).perform()

            time.sleep(x)

            # To City 1
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            a.clear()
            a.send_keys(usr_dest_1)
            time.sleep(x)
            a = driver.find_element(By.XPATH,
                                    '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li''')
            ActionChains(driver).click(a).perform()
            time.sleep(x)

            # Date 1
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            ActionChains(driver).click(a).perform()
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
            time.sleep(x)
            a.send_keys(Keys.BACKSPACE)
            a.send_keys(date_from)
            time.sleep(x)

            # Date done button 1
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button")
            ActionChains(driver).click(a).perform()
            time.sleep(x)


            if flights >= 2:  # To City 2
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input''')
                a.clear()
                a.send_keys(usr_dest_2)
                time.sleep(x)
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
                ActionChains(driver).click(a).perform()
                time.sleep(x)

                # Date 2
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
                ActionChains(driver).click(a).perform()
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
                time.sleep(x)
                a.send_keys(Keys.BACKSPACE)
                a.send_keys(date_to_2)
                time.sleep(x)

                # Date done button 2
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/button")
                ActionChains(driver).click(a).perform()
                time.sleep(x)

            if flights >= 3:  # To City 3
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[1]/div[4]/div/div/div[1]/div/div/input''')
                a.clear()
                a.send_keys(usr_dest_3)
                time.sleep(x)
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[1]/div[6]/div[3]/ul/li[1]''')
                ActionChains(driver).click(a).perform()
                time.sleep(x)

                # Date 3
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
                ActionChains(driver).click(a).perform()
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
                time.sleep(x)
                a.send_keys(Keys.BACKSPACE)
                a.send_keys(date_to_3)
                time.sleep(x)

                # Date done button 3
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button")
                ActionChains(driver).click(a).perform()
                time.sleep(x)

            if flights >= 4:  # To City 4
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[1]/div[4]/div/div/div[1]/div/div/input''')
                a.clear()
                a.send_keys(usr_dest_4)
                time.sleep(x)
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[1]/div[6]/div[3]/ul/li[1]''')
                ActionChains(driver).click(a).perform()
                time.sleep(x)

                # Date 4
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
                ActionChains(driver).click(a).perform()
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
                time.sleep(x)
                a.send_keys(Keys.BACKSPACE)
                a.send_keys(date_to_4)
                time.sleep(x)

                # Date done button 4
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[3]/button")
                ActionChains(driver).click(a).perform()
                time.sleep(x)

            if flights >= 5:  # To City 5
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[1]/div[4]/div/div/div[1]/div/div/input''')
                a.clear()
                a.send_keys(usr_dest_5)
                time.sleep(x)
                a = driver.find_element(By.XPATH,
                                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[1]/div[6]/div[3]/ul/li[1]''')
                ActionChains(driver).click(a).perform()
                time.sleep(x)

                # Date 5
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
                ActionChains(driver).click(a).perform()
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
                time.sleep(x)
                a.send_keys(Keys.BACKSPACE)
                a.send_keys(date_to_5)
                time.sleep(x)

                # Date done button 5
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[2]/div/div[2]/div[2]/div[3]/button")
                ActionChains(driver).click(a).perform()
                time.sleep(x)

# Number of people


a = driver.find_element(By.XPATH,
                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/button")
ActionChains(driver).click(a).perform()
time.sleep(x)

for i in range(adults - 1):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[1]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

for i in range(child):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[2]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

for i in range(infant_seat):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[3]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

for i in range(infant_lap):
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[4]/div/div/span[3]/button")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

a = driver.find_element(By.XPATH,
                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/button[1]")
ActionChains(driver).click(a).perform()
time.sleep(x)

# Type of Class
a = driver.find_element(By.XPATH,
                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[1]")
ActionChains(driver).click(a).perform()
time.sleep(x)
if Class == 2:
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[2]")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

elif Class == 3:
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[3]")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

elif Class == 4:
    a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[4]")
    ActionChains(driver).click(a).perform()
    time.sleep(x)

# Search
a = driver.find_element(By.XPATH,
                        '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button''')
ActionChains(driver).click(a).perform()
time.sleep(x)
