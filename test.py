import unittest
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from login_user import login_user

URL = 'https://scrapinghub.com/crawlera'
USER_NAME = 'testuse1'
USER_PASSWORD = '5gZbuFi..7.2YX5'


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        login_user(self.driver, URL, USER_NAME, USER_PASSWORD)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    def test_open_billing_page(self):
        """
        open Billing page
        """
        driver = self.driver
        billing_button = (
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[@ui-sref='r.o.billing.new']")
                )
            )
        )
        billing_button.click()
        driver.find_element(
            By.XPATH, "//h1[@class='card-header__title'][text()='Crawlera']"
        )


if __name__ == '__main__':
    unittest.main()
