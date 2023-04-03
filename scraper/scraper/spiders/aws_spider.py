import json
import os
import time
from urllib.parse import quote_plus, urlparse

import scrapy
from selenium import webdriver
from selenium.common import exceptions
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class QuotesSpider(scrapy.Spider):

    # os.environ['PATH'] += r"/home/rahul/dev"

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # example
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # example
    # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)
    driver = webdriver.Remote(
        "http://localhost:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
        options=options,
    )

    # # service = Service(executable_path='/snap/bin/chromium.chromedriver')
    # # driver = webdriver.Chrome(service=service)
    driver.get("https://www.amazon.com/")
    driver.implicitly_wait(30)

    what = driver.find_element(by=By.ID, value="twotabsearchtextbox")
    InputFile = "redmi"

    what.send_keys(InputFile)

    driver.implicitly_wait(30)

    search_button = driver.find_element(
        by=By.ID, value="nav-search-submit-button"
    ).click()
    driver.implicitly_wait(30)

    name = "aws"

    start_urls = [driver.current_url]

    def parse(self, response):
        print(response.url)
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        print("dmeo")
