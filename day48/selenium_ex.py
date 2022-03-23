from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

DRIVER_PATH = "/Users/manojshekhawat/Documents/chromedriver"

service = Service(DRIVER_PATH)

driver = webdriver.Chrome(service=service)

driver.get(url=URL)

#driver.find_element(by=By.CSS_SELECTOR, value="#sp-cc-accept").click()

events = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

dict = {}
idx = 0

events = events[0].text.split("\n")
#
print(f"{len(events)}")

for x in events:
    print(f"X:: {x}")

for x in range(0, len(events) -1 , 2):
    dict[idx] = {
        'time': events[x],
        'name': events[x+1]
    }
    idx += 1


print(f"{dict}")

# price = driver.find_element(by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[1]')
# print(f"{price.text}")

#driver.close()
driver.quit()