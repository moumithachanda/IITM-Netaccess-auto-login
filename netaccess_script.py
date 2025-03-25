from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve credentials from .env file
username_input = os.getenv("NETACCESS_USERNAME")
password_input = os.getenv("NETACCESS_PASSWORD")

if not username_input or not password_input:
    print("Error: Username or Password not found in .env file!")
    exit(1)

# Initialize Chrome
driver = webdriver.Chrome()

try:
    # Open NetAccess
    driver.get("https://netaccess.iitm.ac.in/")

    # Wait for the page to load
    time.sleep(2)

    # Find and fill in the username & password fields
    username = driver.find_element(By.NAME, "userLogin")
    password = driver.find_element(By.NAME, "userPassword")

    # Enter credentials
    username.send_keys(username_input)
    password.send_keys(password_input)

    # Press Enter or click login
    password.send_keys(Keys.RETURN)

    print("Login successful. Searching for 'Approve' link...")

    # Wait for the page to load
    time.sleep(3)

    # Find the Approve link by href and click
    approve_link = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/account/approve']"))
    )
    approve_link.click()

    print("Navigated to authorization page. Selecting '1 day' option...")

    # Wait for page load
    time.sleep(2)

    # Find the '1 day' radio button (value="2") and select it
    one_day_option = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='duration' and @value='2']"))
    )
    driver.execute_script("arguments[0].click();", one_day_option)  # Force selection
    time.sleep(1)  # Small delay to ensure selection registers

    # Verify the selection (Debugging Step)
    selected_option = driver.execute_script("return document.querySelector('input[name=duration]:checked').value;")
    print(f"Selected option before clicking authorize: {selected_option}")

    if selected_option != "2":
        raise Exception("1 Day option was not properly selected!")

    print("Selected '1 day'. Clicking 'Authorize' button...")

    # Click the "Authorize" button
    authorize_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Authorize')]"))
    )
    authorize_button.click()

    print("Authorization successful!")

    # Wait to observe the result
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Keep the browser open for debugging
    input("Press Enter to close the browser...")
    driver.quit()