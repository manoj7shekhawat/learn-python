from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

URL = "http://secure-retreat-92358.herokuapp.com/"

DRIVER_PATH = "/Users/manojshekhawat/Documents/chromedriver"

service = Service(DRIVER_PATH)

driver = webdriver.Chrome(service=service)

driver.get(url=URL)

name_input = driver.find_element(by=By.CSS_SELECTOR, value="body > form > input.form-control.top")
name_input.send_keys("Manoj")

last_input = driver.find_element(by=By.CSS_SELECTOR, value="body > form > input.form-control.middle")
last_input.send_keys("Shekhawat")

email_input = driver.find_element(by=By.CSS_SELECTOR, value="body > form > input.form-control.bottom")
email_input.send_keys("manoj7shekhawat@gmail.com")

#name_input.send_keys(Keys.ENTER)
sign_up_btn = driver.find_element(by=By.CSS_SELECTOR, value="body > form > button").click()

time.sleep(10)
driver.quit()
