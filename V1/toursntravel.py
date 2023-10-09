from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from error import error_handle
from api import get_airport_data
from art import *
from radar import *

#PATH = "C:\chromedriver.exe"


def ticket():
    import time
    x = 1.5 # global sleep value
    while True:
        # # Clear screen
        # if os.name == 'nt':  # Windows
        #     os.system('cls')
        # else:
        #     os.system('clear')  # Unix based shells
            
        # Title
        print('*'*100)
        tprint('TravelOn Tours'.center(25))
        print('*'*100)
            
        while True:
            print('='*100)
            print(f"{'1. One Way':^100s}")
            print(f"{'2. Round Trip':^100s}")
            print(f"{'3. Go Back To Main Menu':^100s}")
            print('=' * 100)
            trip = input("Enter your trip selection: ")
            if trip not in ['1','2','3']:
                input("Error: Invalid input (ENTER): ")
                error_handle(101)
            else:
                break

        print('-'*100)
        while True:
            print('*' * 100)
            tprint('TravelOn Tours'.center(25))
            print('*' * 100)
            print('='*100)
            print('1. Economy Class'.center(100))
            print('2. Business Class'.center(100))
            print('3. First Class'.center(100))
            print('=' * 100)
            Class = input('Enter The Class You Would Like To Fly In : ')
            if Class not in ['1','2','3']:
                input("Error: Invalid input (ENTER)")
                error_handle(101)
            else:
                break

        print('-'*100)
        print('*' * 100)
        tprint('TravelOn Tours'.center(25))
        print('*' * 100)
        print('='*100)
        print(f"{'MAX Number Of People is 9':^100s}")
        print(f"{'Minimum 1 Adult should be there':^100s}")
        print(f"{'You Must Have 1 Adult for 2 Infant':^100s}")
        print(f"{'You Can Have Up To 8 Children':^100s}")
        print(f"{'For Each Infant on Lap There Must Be One Adult':^100s}")
        print('='*100)

        while True:
            People_count = 0
            adults = int(input('Enter number of Adult : '))  #Change int to str and impliment it properly
            People_count += adults
            if People_count > 9:
                input("Error: You Can't Have More than 9 people (ENTER): ")
                error_handle(102)
                continue

            child = int(input('Enter number of Child/Children : '))
            People_count += child
            if People_count > 9:
                input("Error: You Can't Have More than 9 people (ENTER): ")
                error_handle(102)
                continue

            infant_seat = int(input('Enter number of Infant : '))
            People_count += infant_seat
            if People_count > 9:
                input("Error: You Can't Have More than 9 people (ENTER): ")
                error_handle(102)
                continue

            infant_lap = int(input('Enter number of Infant on lap : '))
            People_count += infant_lap
            if infant_lap > adults:
                input("Error: For Each Infant on Lap There Must Be One Adult (ENTER)")
                error_handle(103)
            
            if People_count > 9:
                input("Error: You Can't Have More than 9 people (ENTER): ")
                error_handle(102)
                continue
            
            if (infant_lap+infant_seat)/adults > 2:
                input("Error: You Must Have 1 Adult for 2 Infant (ENTER): ")
                error_handle(104)
                continue
            else:
                break

        if trip == '1':  # One Way
            print('*' * 100)
            tprint('TravelOn Tours'.center(25))
            print('*' * 100)
            print('-'*100)
            usr_from = input('Enter -From- location : ')
            usr_from = get_airport_data(usr_from)
                        
            usr_dest = input('Enter -Destination- : ')
            usr_dest = get_airport_data(usr_dest)
            
            date_from = input('Enter Date of flight (dd/mm/yyyy) :')

        elif trip == '2':  # Round Trip
            print('*' * 100)
            tprint('TravelOn Tours'.center(25))
            print('*' * 100)
            print('-' * 100)
            usr_from = input('Enter -From- location : ')
            usr_from = get_airport_data(usr_from)
            
            usr_dest = input('Enter -Destination- : ')
            usr_dest = get_airport_data(usr_dest)
            
            date_from = input('Enter Date of First Flight (dd/mm/yyyy) :')
            date_to = input('Enter Date of Second Flight (dd/mm/yyyy) :')

        #elif trip == '4':
            # flights = int(input('Enter Number of flights : '))  #Change int to str and impliment it properly
            
            # usr_from = input('Enter -From- location : ')
            # usr_from = get_airport_data(usr_from)
            
            # usr_dest_1 = input('Enter -Destination- 1 : ')
            # usr_dest_1 = get_airport_data(usr_dest_1)
            
            # date_from = input('Enter Date of First Flight (dd/mm/yyyy) :')

            # if flights >= 2:
            #     usr_dest_2 = input('Enter -Destination- 2 : ')
            #     usr_dest_2 = get_airport_data(usr_dest_2)
                
            #     date_to_2 = input('Enter Date of Second Flight (dd/mm/yyyy) :')

            # if flights >= 3:
            #     usr_dest_3 = input('Enter -Destination- 3 : ')
            #     usr_dest_3 = get_airport_data(usr_dest_3)
                
            #     date_to_3 = input('Enter Date of Third Flight (dd/mm/yyyy) :')

            # if flights >= 4:
            #     usr_dest_4 = input('Enter -Destination- 4 : ')
            #     usr_dest_4 = get_airport_data(usr_dest_4)
                
            #     date_to_4 = input('Enter Date of Fourth Flight (dd/mm/yyyy) :')

            # if flights >= 5:
            #     usr_dest_5 = input('Enter -Destination- 5 : ')
            #     usr_dest_5 = get_airport_data(usr_dest_5)
                
            #     date_to_5 = input('Enter Date of Final Flight (dd/mm/yyyy) :')


        flag_1 = True

        options = Options()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        driver.get('https://www.google.com/travel/flights')
        driver.implicitly_wait(10)


        a = driver.find_element(By.XPATH,
                                "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]")
        driver.implicitly_wait(10)
        ActionChains(driver).click(a).perform()

        if trip == '1':  # One Way
            b = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]")
            time.sleep(x)
            ActionChains(driver).click(b).perform()
        elif trip == '2':  # Round trip
            c = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[1]")
            time.sleep(x)
            ActionChains(driver).click(c).perform()
        #elif trip == '3':  # Multi City
            # d = driver.find_element(By.XPATH,
            #                         "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[3]")
            # time.sleep(x)
            # ActionChains(driver).click(d).perform()


        if trip == '1':  # One Way
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
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button")
            ActionChains(driver).click(a).perform()
            time.sleep(x)



        elif trip == '2':  # Round Trip
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
            a.send_keys(Keys.ENTER)
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
            a = driver.find_element(By.XPATH,
                            "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button")
            ActionChains(driver).click(a).perform()
            time.sleep(x)


        #elif trip == '3': #Multi city
            # Add Flight
            # time.sleep(x)
            # a = driver.find_element(By.XPATH,
            #                         '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/button''')
            # for i in range(flights - 2):
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            # # From City
            # a = driver.find_element(By.XPATH,
            #                         '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div/input''')
            # a.clear()
            # a.send_keys(usr_from)
            # time.sleep(x)
            # a = driver.find_element(By.XPATH,
            #                         '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li[1]''')
            # ActionChains(driver).click(a).perform()

            # time.sleep(x)

            # # To City 1
            # a = driver.find_element(By.XPATH,
            #                         '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            # a.clear()
            # a.send_keys(usr_dest_1)
            # time.sleep(x)
            # a = driver.find_element(By.XPATH,
            #                         '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[6]/div[3]/ul/li''')
            # ActionChains(driver).click(a).perform()
            # time.sleep(x)

            # # Date 1
            # a = driver.find_element(By.XPATH,
            #                         "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            # ActionChains(driver).click(a).perform()
            # a = driver.find_element(By.XPATH,
            #                         "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
            # time.sleep(x)
            # a.send_keys(Keys.BACKSPACE)
            # a.send_keys(date_from)
            # a.send_keys(Keys.ENTER)
            # time.sleep(x)

            # # Date done button 1
            # a = driver.find_element(By.XPATH,
            #                         "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button")
            # ActionChains(driver).click(a).perform()
            # time.sleep(x)


            # if flights >= 2:  # To City 2
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            #     a.clear()
            #     a.send_keys(usr_dest_2)
            #     time.sleep(x)
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]''')
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            #     # Date 2
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            #     ActionChains(driver).click(a).perform()
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
            #     time.sleep(x)
            #     a.send_keys(Keys.BACKSPACE)
            #     a.send_keys(date_to_2)
            #     a.send_keys(Keys.ENTER)
            #     time.sleep(x)

            #     # Date done button 2
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/button")
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            # if flights >= 3:  # To City 3
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            #     a.clear()
            #     a.send_keys(usr_dest_3)
            #     time.sleep(x)
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[1]/div[6]/div[3]/ul/li[1]''')
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            #     # Date 3
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            #     ActionChains(driver).click(a).perform()
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
            #     time.sleep(x)
            #     a.send_keys(Keys.BACKSPACE)
            #     a.send_keys(date_to_3)
            #     a.send_keys(Keys.ENTER)
            #     time.sleep(x)

            #     # Date done button 3
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button")
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            # if flights >= 4:  # To City 4
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            #     a.clear()
            #     a.send_keys(usr_dest_4)
            #     time.sleep(x)
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[1]/div[6]/div[3]/ul/li[1]''')
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            #     # Date 4
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            #     ActionChains(driver).click(a).perform()
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
            #     time.sleep(x)
            #     a.send_keys(Keys.BACKSPACE)
            #     a.send_keys(date_to_4)
            #     a.send_keys(Keys.ENTER)
            #     time.sleep(x)

            #     # Date done button 4
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[3]/button")
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            # if flights >= 5:  # To City 5
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[1]/div[4]/div/div/div[1]/div/div/input''')
            #     a.clear()
            #     a.send_keys(usr_dest_5)
            #     time.sleep(x)
            #     a = driver.find_element(By.XPATH,
            #                             '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[1]/div[6]/div[3]/ul/li[1]''')
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)

            #     # Date 5
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input")
            #     ActionChains(driver).click(a).perform()
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input")
            #     time.sleep(x)
            #     a.send_keys(Keys.BACKSPACE)
            #     a.send_keys(date_to_5)
            #     a.send_keys(Keys.ENTER)
            #     time.sleep(x)

            #     # Date done button 5
            #     a = driver.find_element(By.XPATH,
            #                             "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[5]/div[2]/div/div[2]/div[2]/div[3]/button")
            #     ActionChains(driver).click(a).perform()
            #     time.sleep(x)
                

        # Number of people
        if not (adults == 1 and child == 0 and infant_lap == 0 and infant_seat == 0):
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
        if Class in ['2','3','4']:
            a = driver.find_element(By.XPATH,
                                    "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[1]")
            ActionChains(driver).click(a).perform()
            time.sleep(x)
            if Class == '2':
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[3]")
                ActionChains(driver).click(a).perform()
                time.sleep(x)

            elif Class == '3':
                a = driver.find_element(By.XPATH,
                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[4]")
                ActionChains(driver).click(a).perform()
                time.sleep(x)


        # Search
        a = driver.find_element(By.XPATH,
                                '''/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button''')
        ActionChains(driver).click(a).perform()
        time.sleep(6)

        # Retrieving data
        #1st deal
        air1=driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[2]/span')
        dura1=driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[3]/div')
        time1p1=driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span')
        time1p2=driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span')
        stops1=driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[4]/div[1]/span')
        price1=driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span')

        #2nd deal
        air2 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[2]')
        dura2 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[3]/div')
        time2p1 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span')
        time2p2 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span')
        stops2 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[4]/div[1]/span')
        price2 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[2]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span')

        #3rd deal
        air3 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[2]')
        dura3 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[3]/div')
        time3p1 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[1]/span/span/span')
        time3p2 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[2]/div[1]/span/span[2]/span/span/span')
        stops3 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[4]/div[1]/span')
        price3 = driver.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[3]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span')
        #printing
        print('*' * 100)
        tprint('TravelOn Tours'.center(25))
        print('*' * 100)
        print()
        g26 = " " * 26
        print("=" * 100)
        print('*' * 37, end='')
        print(f"{'1st DEAL':^26s}", end='')
        print(f"{'*' * 37:^20}")
        print(f"{'Time:':^37s}{'Flight Duration:':^26s}{'Stops:':^37s}")
        time = (time1p1.text, time1p2.text)
        jtime = "-".join(time)
        print(f"{jtime:^37s}{dura1.text:^26s}{stops1.text:^37s}")
        print()
        print(f"{'Airlines:':^50}{'Ticket Price (KWD):':^50}")
        print(f"{air1.text:^50}{price1.text:^50}")
        print("-" * 100)
        print('*' * 37, end='')
        print(f"{'2nd DEAL':^26s}", end='')
        print(f"{'*' * 37:^20}")
        print(f"{'Time:':^37s}{'Flight Duration:':^26s}{'Stops:':^37s}")
        time2 = (time2p1.text, time2p2.text)
        jtime2 = "-".join(time2)
        print(f"{jtime2:^37s}{dura2.text:^26s}{stops2.text:^37s}")
        print()
        print(f"{'Airlines:':^50}{'Ticket Price (KWD):':^50}")
        print(f"{air2.text:^50}{price2.text:^50}")
        print("-"*100)
        print('*' * 37, end='')
        print(f"{'3rd DEAL':^26s}", end='')
        print(f"{'*' * 37:^20}")
        print(f"{'Time:':^37s}{'Flight Duration:':^26s}{'Stops:':^37s}")
        time3 = (time3p1.text, time3p2.text)
        jtime3 = "-".join(time3)
        print(f"{jtime3:^37s}{dura3.text:^26s}{stops3.text:^37s}")
        print()
        print(f"{'Airlines:':^50}{'Ticket Price (KWD):':^50}")
        print(f"{air3.text:^50}{price3.text:^50}")
        print("="*100)
        radar(usr_from, usr_dest)
        
def radar(usr_from, usr_dest):
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
    driver.find_element(By.XPATH, '//*[@id="flight_by_route_from"]').send_keys(usr_from)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/ul/li/a/span[1]').click()
    time.sleep(2)

    # arrival
    driver.find_element(By.XPATH, '//*[@id="flight_by_route_to"]').send_keys(usr_dest)
    time.sleep(1)
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