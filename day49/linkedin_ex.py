import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.linkedin.com/"

DRIVER_PATH = "/Users/manojshekhawat/Documents/chromedriver"

EMAIL_ID = os.environ.get("EMAIL_ID")
PASSWD = os.environ.get("PASSWD")

service = Service(DRIVER_PATH)

driver = webdriver.Chrome(service=service)

driver.get(url=URL)

email_input = driver.find_element(by=By.ID, value="session_key")
email_input.send_keys(EMAIL_ID)

pwd_input = driver.find_element(by=By.ID, value="session_password")
pwd_input.send_keys(PASSWD)

sign_in_btn = driver.find_element(by=By.CSS_SELECTOR, value=".sign-in-form__submit-button")
sign_in_btn.click()

job_link = driver.find_element(by=By.ID, value="ember20")
job_link.click()

time.sleep(20)

driver.quit()