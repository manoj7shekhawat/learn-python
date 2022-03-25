import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_UP = 300
PROMISED_DOWN = 300
CHROME_DRIVER_PATH = "/Users/manojshekhawat/Documents/chromedriver"

TWITTER_URL = "https://twitter.com/"
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self):
        super().__init__()

        service = Service(CHROME_DRIVER_PATH)
        self._driver = webdriver.Chrome(service=service)

        self._down = 0
        self._up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")

        consent_btn = self.driver.find_element(by=By.ID, value="_evidon-banner-acceptbutton")
        consent_btn.click()

        go_link = self.driver.find_element(by=By.CSS_SELECTOR, value=".js-start-test")
        go_link.click()

        # wait for some time
        time.sleep(45)

        # Click:: Back to test results
        self.driver.find_element(by=By.LINK_TEXT, value="Back to test results").click()

        # internet speed
        down_txt = self.driver.find_element(by=By.XPATH,
                                            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up_txt = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        # Call setter methods
        self.up = up_txt.text
        self.down = down_txt.text

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)

        time.sleep(10)
        # accept cookies
        accept_cookies = self.driver.find_element(by=By.XPATH,
                                                  value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span')
        accept_cookies.click()

        # Sign In
        sign_in = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()
        time.sleep(5)

        # Input email id
        input_email = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        input_email.send_keys(TWITTER_EMAIL)

        # Next button
        nxt_btn = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
        nxt_btn.click()
        time.sleep(25)

        # Enter password
        passwd_ipt = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwd_ipt.send_keys(TWITTER_PASSWD)

        # Login
        login_btn = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span')
        login_btn.click()

        time.sleep(5)
        # Tweet text
        tweet_txt = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_txt.send_keys(f"By Twitter Bot:: My Internet Download speed: {self.down} and Upload speed: {self.up}. Less then promised by ISP")
        time.sleep(3)

        # Tweet button
        tweet_btn = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()

    @property
    def driver(self):
        return self._driver

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value

    @property
    def up(self):
        return self._up

    @up.setter
    def up(self, value):
        self._up = value


istb = InternetSpeedTwitterBot()
istb.get_internet_speed()

print(f"Down:: {istb.down}\nUp:: {istb.up}")

time.sleep(5)

istb.tweet_at_provider()
print("Tweeted, please check")

time.sleep(10)

istb.driver.quit()
