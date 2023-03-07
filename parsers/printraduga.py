from parser_classes.selenium_parser import __SeleniumParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class printradugaParser(__SeleniumParser):
    def __init__(self, size, counts, proxy):
        self.parsing_page = "https://www.printraduga.com/pechat-nakleek/obemnie/"
        super().__init__(size, counts, proxy)

    def parse(self, container: list) -> None:
        self.get(self.parsing_page)

        width = self.wait('width', 30, By.NAME)
        height = self.find('diament', By.NAME)
        count_input = self.find('count', By.NAME)

        width.clear()
        height.clear()
        width.send_keys(str(self.size))
        height.send_keys(str(self.size))

        costs = []
        for count in self.counts:
            count_input.clear()
            count_input.send_keys(count)
            count_input.click()
            width.click()
            height.click()
            sleep(0.5)
            cost = self.find('p[class="priceAll"]')
            costs.append(float(cost.text.replace(" руб", "")))

        container.append(("PRINTRADUGA", costs))
