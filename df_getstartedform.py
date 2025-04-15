from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://designforce.co/how-it-works/get-designers-form/")
try:
    # Wait until the cookie banner's "Reject" button is clickable
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reject All']")))

    # Click the "Reject" button
    accept_button.click()
    print("Cookie banner rejected successfully.")
except Exception as e:
    print("Cookie banner not found or could not be rejected:", e)

checkbox_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div/div[1]/label/span')
checkbox2_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div/div[11]/label/span')
checkbox3_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div/div[17]/label/span')
next_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/div[2]/div[1]/div/form/div[2]/div[2]/button')

checkbox_button.click()
time.sleep(5)
checkbox2_button.click()
time.sleep(5)
checkbox3_button.click()
time.sleep(5)
next_button.click()

time.sleep(15)

firstname_field = driver.find_element(By.ID, "first_name")
lastname_field = driver.find_element(By.ID, "last_name")
emailaddress_field = driver.find_element(By.ID, "work_email_address")
phone_field = driver.find_element(By.ID, "phone" )
company_field = driver.find_element(By.ID, "your_company")
requirements_field = driver.find_element(By.ID, "what_are_your_requirements_for_the_design")
radio_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/div[2]/div[1]/div/form/div[3]/div[6]/div[2]/div[3]/label/span')
submit_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/div[2]/div[1]/div/form/div[3]/div[7]/div/div[2]/div/div/button')

firstname_field.send_keys("April")
lastname_field.send_keys("Six")
time.sleep(5)
emailaddress_field.send_keys("leizel+66@500designs.com")
time.sleep(5)
phone_field.send_keys("09782645543")
time.sleep(5)
company_field.send_keys("Designs50000")
time.sleep(5)
requirements_field.send_keys("sample submission only")
time.sleep(5)
radio_button.click()
time.sleep(5)
submit_button.click()

time.sleep(15)

print("Form submitted successfully")

driver.quit()