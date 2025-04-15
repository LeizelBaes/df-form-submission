from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://designforce.co/contact-us/")
try:
    # Wait until the cookie banner's "Reject" button is clickable
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reject All']")))

    # Click the "Reject" button
    accept_button.click()
    print("Cookie banner rejected successfully.")
except Exception as e:
    print("Cookie banner not found or could not be rejected:", e)

selection_input = driver.find_element(By.XPATH, '//*[@id="typeOfInquiry"]/option[3]')
firstname_field = driver.find_element(By.ID, "first_name")
lastname_field = driver.find_element(By.ID, "last_name")
emailaddress_field = driver.find_element(By.ID, "work_email_address")
company_field = driver.find_element(By.ID, "your_company")
inquiry_field = driver.find_element(By.ID, "message")
send_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/div/div[2]/div/form/div[6]/div/button')

selection_input.click()
time.sleep(5)
firstname_field.send_keys("Sixth")
lastname_field.send_keys("April")
time.sleep(5)
emailaddress_field.send_keys("leizel+67@500designs.com")
company_field.send_keys("5000Designss")
time.sleep(5)
inquiry_field.send_keys("This is a sample inquiry")
send_button.click()

time.sleep(15)

print("Form submitted successfully")

driver.quit()