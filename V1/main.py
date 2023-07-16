from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open Akbar Travels website
driver.get('https://www.akbartravels.com/kw/flight?lan=en')

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'form-partial')))

# Input the beginning location
begin_location = driver.find_element(By.ID, 'fromCity')
begin_location.clear()
begin_location.send_keys('Your Beginning Location')

# Input the final destination
final_destination = driver.find_element(By.ID, 'toCity')
final_destination.clear()
final_destination.send_keys('Your Final Destination')

# Click the search button
search_button = driver.find_element(By.XPATH, "//button[contains(text(),'Search')]")
search_button.click()

# Wait for the search results to load
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='fltrt-tabs']")))

# Get the list of available airline tickets
tickets = driver.find_elements(By.XPATH, "//div[@class='flight-result-list']//li")
for ticket in tickets:
    print(ticket.text)

# Close the WebDriver
driver.quit()