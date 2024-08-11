import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the Excel file
df = pd.read_excel('C:/Users/jadha/OneDrive/Desktop/selenium/dummy_data_entry_15_rows.xlsx')  # Replace 'file_path.xlsx' with the path to your Excel file

# Set up the WebDriver (ensure that you have ChromeDriver installed and it's in your PATH)
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get('C:/Users/jadha/OneDrive/Desktop/selenium/data_input.html')  # Replace 'http://website-url.com' with the actual URL of the website

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        for header in df.columns:
            # Find the input field by name, id, or other attribute
            input_field = driver.find_element(By.NAME, header)  # Update the find_element method according to the actual field names

            # Fill the input field with data from the corresponding cell in the row
            input_field.send_keys(str(row[header]))

        # If there are dropdowns or radio buttons, handle them here
        # Example for a dropdown
        #dropdown = driver.find_element(By.NAME, 'dropdown_name')  # Replace 'dropdown_name' with the actual name
        #dropdown.send_keys('option_text')  # Replace 'option_text' with the option you want to select

        # Example for a radio button
        ##radio_button.click()

        # Submit the form or save the data
        submit_button = driver.find_element(By.NAME, 'submit_button_name')  # Replace 'submit_button_name' with the actual name
        submit_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
