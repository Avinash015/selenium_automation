from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your WebDriver
driver_path = 'C:\\Users\\jadha\\OneDrive\\Desktop\\selenium\\chromedriver.exe'

# Initialize WebDriver with service and options
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Open the URL
driver.get("file:///C:/Users/jadha/OneDrive/Desktop/selenium/multiple_select1.html")

# Function to select an option in the dropdown
def select_option(option_text):
    # Open the dropdown
    dropdown_button = driver.find_element(By.CSS_SELECTOR, '.e_multi_select_wrapper > div')
    dropdown_button.click()
    
    # Wait until the dropdown options are visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dropdown-content')))
    
    # Find the option by its text and click it
    option = driver.find_element(By.XPATH, f"//span[contains(text(), '{option_text}')]")
    option.click()
    
    # Close the dropdown (optional)
    dropdown_button.click()

# Select specific options
select_option('Option 1')
select_option('Option 3')

# Verify the selected options
selected_text = driver.find_element(By.CSS_SELECTOR, '.e_multi_select_wrapper > div').text
print(f"Selected options: {selected_text.encode('ascii', 'ignore').decode('ascii')}")


# Close the browser after a short delay
time.sleep(3000)
driver.quit()
