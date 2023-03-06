import selenium
import undetected_chromedriver
from parser_classes.selenium_parser import __SeleniumParser
from selenium import webdriver
import undetected_chromedriver as uc


class __UndetectedParser(__SeleniumParser):
    def __init__(self, size, counts, proxy) -> None:
        super().__init__(size, counts, proxy)
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--proxy-server=%s' % self.proxy)
        self.driver = uc.Chrome(options=options, headless=True)
