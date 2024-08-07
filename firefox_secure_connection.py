from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Path to your WebDriver
driver_path = 'C:\\Users\\jadha\\OneDrive\\Desktop\\selenium\\geckodriver.exe'

# Initialize WebDriver with service and options
service = Service(driver_path)
options = Options()
options.set_capability('acceptInsecureCerts', True)

driver = webdriver.Firefox(service=service, options=options)
driver.implicitly_wait(10)

# Open the URL
driver.get("https://expired.badssl.com/")

# Print the text of the h1 element
print(driver.find_element(By.TAG_NAME, 'h1').text)

# Close the browser after a short delay
time.sleep(3)
driver.quit()
