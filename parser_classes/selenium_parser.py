import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from parser_classes.main_parser import __mainParser


class __SeleniumParser(__mainParser):
    def __init__(self, size, counts, proxy) -> None:
        super().__init__(size, counts, proxy)
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument('--proxy-server=%s' % self.proxy)`
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options, service=Service(
            ChromeDriverManager().install()))

    def get(self, url):
        self.driver.get(url)

    def wait(self, elem_, time=5, by=By.CSS_SELECTOR) -> WebElement:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((by, elem_)))

    def wait_all(self, elem_, time=5, by=By.CSS_SELECTOR) -> list[WebElement]:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located((by, elem_)))

    def find(self, elem_, by=By.CSS_SELECTOR) -> WebElement:
        return self.driver.find_element(by, elem_)

    def find_all(self, elem_, by=By.CSS_SELECTOR) -> list[WebElement]:
        return self.driver.find_elements(by, elem_)

    def to_select(self, elem_) -> Select:
        return Select(elem_)

    def parse(self, container: list) -> None:
        pass
