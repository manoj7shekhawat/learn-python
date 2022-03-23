from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

DRIVER_PATH = "/Users/manojshekhawat/Documents/chromedriver"

service = Service(DRIVER_PATH)

driver = webdriver.Chrome(service=service)

driver.get(url=URL)

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)").text

print(f"Articles: {article_count}")

driver.quit()
