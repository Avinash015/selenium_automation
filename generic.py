import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the Excel file
file_path = 'C:/Users/jadha/OneDrive/Desktop/selenium/dummy_data_entry_15_rows.xlsx'
df = pd.read_excel(file_path)

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the website
website_url = 'C:/Users/jadha/OneDrive/Desktop/selenium/data_input.html'
driver.get(website_url)

# List to cache labels that have no matching input fields
input_field_cache = []

# Helper function to find input fields based on various attributes
def find_input_field(driver, label):
    # Check if label already exists in the input_field_cache list
    if label in input_field_cache:
        print(f"Skipping search for {label} as it's already marked as not found.")
        return None

    search_labels = [label, label.lower()]  # Original and lowercase label

    for search_label in search_labels:
        try:
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, 
                     f"//input[@name='{search_label}'] | "
                     f"//input[@placeholder='{search_label}'] | "
                     f"//input[@aria-label='{search_label}'] | "
                     f"//input[@id='{search_label}'] | "
                     f"//label[contains(text(), '{search_label}')]/following-sibling::input | "
                     f"//textarea[@name='{search_label}'] | "
                     f"//textarea[@placeholder='{search_label}'] | "
                     f"//textarea[@aria-label='{search_label}'] | "
                     f"//textarea[@id='{search_label}'] | "
                     f"//div[contains(@class, 'input') and contains(text(), '{search_label}')]/following-sibling::input | "
                     f"//div[contains(@class, 'textarea') and contains(text(), '{search_label}')]/following-sibling::textarea"
                    )
                )
            )
            return input_field
        except Exception:
            continue  # Try the next label variation if the current one fails

    # If no matching input field is found, add the label to the cache list
    print(f"No matching input field found for label: {label} or its lowercase version.")
    input_field_cache.append(label)
    return None

try:
    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        for header in df.columns:
            # Check if the data for the current header is missing (NaN)
            if pd.isna(row[header]):
                print(f"Skipping input for {header} as data is missing for row {index + 1}")
                continue  # Skip if data is missing

            # Attempt to find the input field using the header (original and lowercase)
            input_field = find_input_field(driver, header)
            if input_field:
                input_field.send_keys(str(row[header]))
            else:
                print(f"Field for header '{header}' not found. Data will not be entered.")

        # Locate the submit button using XPath for both <input type='submit'> and <button type='submit'>
        try:  
            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 
                     "input[type='submit'], button[type='submit'], button.submit-btn, input[name='submit_button_name'], button[name='submit_button_name']"
                    )
                )
            )
            submit_button.click()
        except Exception as e:
            print(f"An error occurred locating or clicking the submit button: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
