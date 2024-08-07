from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your WebDriver
driver_path = 'C:\\Users\\jadha\\OneDrive\\Desktop\\selenium\\chromedriver.exe'

# Set Chrome options

chrome_options = Options()
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.set_capability('acceptInsecureCerts', True)

# Initialize WebDriver with service and options
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)

# Open the URL
driver.get("https://expired.badssl.com/")

# Print the text of the h1 element
print(driver.find_element(By.TAG_NAME, 'h1').text)

# Close the browser after a short delay
time.sleep(3)
driver.quit()
