import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the Excel file
df = pd.read_excel('C:/Users/jadha/OneDrive/Desktop/selenium/dummy_data_entry_15_rows.xlsx')

# Set up the WebDriver
driver = webdriver.Chrome()

# List of headers to ignore completely
ignore_headers = ['Location', 'Another_Irrelevant_Header']  # Add any headers that should be skipped entirely

# Helper function to find input fields based on multiple attributes and approaches
def find_input_field(driver, label):
    search_labels = [label, label.lower()]  # Original and lowercase label

    for search_label in search_labels:
        try:
            input_field = WebDriverWait(driver, 5).until(
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

    print(f"No matching input field found for label: {label} or its lowercase version.")
    return None

try:
    # Open the website
    driver.get('C:/Users/jadha/OneDrive/Desktop/selenium/data_input.html')

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        for header in df.columns:
            if header in ignore_headers:
                print(f"Skipping header: {header}")
                continue  # Skip the current header if it's in the ignore list

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

        # Example for submitting the form
        submit_button = driver.find_element(By.NAME, 'submit_button_name')  # Replace with actual name
        submit_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
