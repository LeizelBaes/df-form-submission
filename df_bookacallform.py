from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://designforce.co/book-a-call/")
try:
    # Wait until the cookie banner's "Reject" button is clickable
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reject All']")))

    # Click the "Reject" button
    accept_button.click()
    print("Cookie banner rejected successfully.")
except Exception as e:
    print("Cookie banner not found or could not be rejected:", e)

firstname_field = driver.find_element(By.ID, "first_name")
lastname_field = driver.find_element(By.ID, "last_name")
emailaddress_field = driver.find_element(By.ID, "work_email_address")
phone_field = driver.find_element(By.ID, "phone")
company_field = driver.find_element(By.ID, "your_company")
inquiry_field = driver.find_element(By.ID, "how_did_you_first_hear_about_us")
radio_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div[2]/div[3]/div/form/div[6]/div[2]/div[1]/label/span')

firstname_field.send_keys("First")
lastname_field.send_keys("Last")
time.sleep(5)
emailaddress_field.send_keys("leizel+65@500designs.com")
phone_field.send_keys("092646362")
company_field.send_keys("500Designss")
time.sleep(5)
inquiry_field.send_keys("sample inquiry")
time.sleep(5)
radio_button.click()

time.sleep(10)
submit_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div[2]/div[3]/div/form/div[7]/div/button')
submit_button.click()

time.sleep(10)  # Wait for the page to load

print("Form submitted successfully")

driver.quit()
