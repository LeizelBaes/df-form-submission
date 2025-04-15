from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://designforce.co/blog/")
try:
    # Wait until the cookie banner's "Reject" button is clickable
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reject All']")))

    # Click the "Reject" button
    accept_button.click()
    print("Cookie banner rejected successfully.")
except Exception as e:
    print("Cookie banner not found or could not be rejected:", e)

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("test0406@gmail.com")
time.sleep(10)
subscribe_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div[2]/div[2]/div[4]/div/form/div[1]/div[2]/div/div/button')
subscribe_button.click()

time.sleep(15)

print("Subscribed")

driver.quit()