from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

DRIVER_PATH = "/Users/manojshekhawat/Documents/chromedriver"

service = Service(DRIVER_PATH)

driver = webdriver.Chrome(service=service)

driver.get(url=URL)

cookie = driver.find_element(by=By.ID, value="cookie")

timeout = time.time() + 60 * 5  # 5 minutes from now

secs_5 = time.time() + 5


def is_grayed(elem_id):
    element = driver.find_element(by=By.ID, value=elem_id)
    ele_class = element.get_attribute("class")
    if ele_class == "grayed":
        return True
    else:
        return False


while True:
    cookie.click()
    if time.time() > timeout:
        break
    if time.time() > secs_5:
        print("5 Secs. Checking divs")
        div_ids = ["buyElder Pledge", "buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine",
                   "buyFactory", "buyGrandma", "buyCursor"]
        for div in div_ids:
            is_grey = is_grayed(div)
            if not is_grey:
                driver.find_element(by=By.ID, value=div).click()
                print(f"Clicked: {div}")
                break
        secs_5 = time.time() + 5

score = driver.find_element(by=By.ID, value="cps").text
print(f"Your score: {score}")
driver.quit()
