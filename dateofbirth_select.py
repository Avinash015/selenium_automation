from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your WebDriver
driver_path = 'C:\\Users\\jadha\\OneDrive\\Desktop\\selenium\\chromedriver.exe'

# Initialize WebDriver with service and options
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Open the URL
driver.get("file:///C:/Users/jadha/OneDrive/Desktop/selenium/calendar.html")

# Define the target date of birth
dob = "1995-08-15"  # Format: YYYY-MM-DD

# Locate the date input field
date_input = driver.find_element(By.ID, "birthday")

# Use JavaScript to set the value of the date input
driver.execute_script(f"arguments[0].value = '{dob}';", date_input)

# Optionally, verify the date input value
assert date_input.get_attribute("value") == dob, "Date of Birth was not set correctly."


# Close the browser after a short delay
time.sleep(3000)
driver.quit()
