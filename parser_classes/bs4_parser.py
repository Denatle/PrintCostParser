from bs4 import BeautifulSoup
from parser_classes.main_parser import __mainParser
import requests


class __bs4Parser(__mainParser):
    def __init__(self, size, counts, proxy):
        super().__init__(size, counts, proxy)

    def get(self, url) -> BeautifulSoup:
        return BeautifulSoup(requests.get(url).text, "lxml")

    def parse(self, container: list) -> None:
        pass

    def quit(self):
        pass
