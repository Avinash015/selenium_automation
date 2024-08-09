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
driver.get("file:///C:/Users/jadha/OneDrive/Desktop/selenium/multiple_select.html")


# Click on the dropdown button to show options
dropdown_button = driver.find_element(By.XPATH, "//button[contains(text(),'Select Options')]")
dropdown_button.click()

# Wait for the dropdown options to be visible
time.sleep(1)

# Select checkboxes based on their value
options_to_select = ["Option 1", "Option 3"]  # Replace with the options you want to select

for option in options_to_select:
    checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{option}')]/input[@type='checkbox']")
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    
    # Click the checkbox using JavaScript
    driver.execute_script("arguments[0].click();", checkbox)

# Wait to observe the changes (only needed if you're running this script without headless mode)
time.sleep(2)

# Verify selections (Optional)
selected_items = driver.find_elements(By.CSS_SELECTOR, ".selected-items div")
selected_values = [item.text for item in selected_items]
print("Selected options:", selected_values)
# Close the browser after a short delay
time.sleep(3000)
driver.quit()
