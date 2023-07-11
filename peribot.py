import json
from datetime import datetime
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load configuration from config.json file
with open('config.json') as config_file:
    config = json.load(config_file)

# Extract values from the config
address = config['address']
username = config['username']
password = config['password']

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(address)
print(f"Opened login page: {address}")

# Find the login form elements
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txtUserId')))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txtPassword')))
checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ckAgree')))

# Fill in the login form fields
username_input.send_keys(username)
password_input.send_keys(password)
checkbox.click()
print("Filled in login form.")

# Submit the login form
login_form = driver.find_element(By.TAG_NAME, 'form')
login_form.submit()
print("Submitted the login form.")

# Wait for the new page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("New page loaded after login.")

# Wait before saving the response
wait_time = 3  # seconds
time.sleep(wait_time)

# Save the response as an HTML file
html_results_folder = "./html_results"
os.makedirs(html_results_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Generate the filename based on the current date and time
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d-%H-%M")

# Find the next available sequential number
existing_files = os.listdir(html_results_folder)
sequential_number = 0
while True:
    filename = f"{formatted_date}_result{sequential_number:03d}.html"
    filepath = os.path.join(html_results_folder, filename)
    if filename not in existing_files:
        break
    sequential_number += 1

# Save the response content to the HTML file
with open(filepath, "w", encoding="utf-8") as file:
    file.write(driver.page_source)

print(f"Response saved as HTML file: {filepath}")

# Navigate to the eco_page.php?id=ba664e2a-5395-11ea-9959-1255a22fd2a3 page
eco_page_url = address + "eco_page.php?id=ba664e2a-5395-11ea-9959-1255a22fd2a3"
driver.get(eco_page_url)
print(f"Opened eco_page: {eco_page_url}")

# Wait for the new page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("New page loaded after navigating to eco_page.")

# Wait before saving the response
wait_time = 3  # seconds
time.sleep(wait_time)

# Generate the filename for the eco_page result
filename = f"{formatted_date}_eco_result{sequential_number:03d}.html"
filepath = os.path.join(html_results_folder, filename)

# Save the response content to the HTML file
with open(filepath, "w", encoding="utf-8") as file:
    file.write(driver.page_source)

print(f"Response saved as HTML file: {filepath}")

# Find links with text containing "Happy Birthday"
birthday_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Happy Birthday')]")
if birthday_links:
    print("Links with text containing 'Happy Birthday':")
    birthday_link_urls = [link.get_attribute('href') for link in birthday_links]
    for link_url in birthday_link_urls:
        print(link_url)

        # Go to the birthday link page
        driver.get(link_url)
        print(f"Opened birthday link: {link_url}")

        # Wait for the new page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        print("New page loaded after navigating to birthday link.")

        # Wait before saving the response
        wait_time = 3  # seconds
        time.sleep(wait_time)

        # Find the comment input field with the name "message"
        comment_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'message')))

        # Clear the input field (if needed)
        comment_input.clear()

        # Submit a message saying "Happy birthday!"
        comment_input.send_keys("Happy birthday!")
        comment_input.submit()
        print("Submitted birthday message.")

        # Random delay between 1 and 5 seconds
        random_delay = random.randint(1, 5)
        print(f"Waiting for {random_delay} seconds before the next message.")
        time.sleep(random_delay)

        # Go back to the eco_page
        driver.back()

# Find links with text containing "Year Anniversary"
anniversary_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Year Anniversary')]")
if anniversary_links:
    print("Links with text containing 'Year Anniversary':")
    anniversary_link_urls = [link.get_attribute('href') for link in anniversary_links]
    for link_url in anniversary_link_urls:
        print(link_url)

        # Go to the anniversary link page
        driver.get(link_url)
        print(f"Opened anniversary link: {link_url}")

        # Wait for the new page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        print("New page loaded after navigating to anniversary link.")

        # Wait before saving the response
        wait_time = 3  # seconds
        time.sleep(wait_time)

        # Find the comment input field with the name "message"
        comment_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'message')))

        # Clear the input field (if needed)
        comment_input.clear()

        # Submit a message saying "Happy anniversary!"
        comment_input.send_keys("Happy anniversary!")
        comment_input.submit()
        print("Submitted anniversary message.")

        # Random delay between 1 and 5 seconds
        random_delay = random.randint(1, 5)
        print(f"Waiting for {random_delay} seconds before the next message.")
        time.sleep(random_delay)

        # Go back to the eco_page
        driver.back()

# Close the browser
driver.quit()
print("Browser closed.")
