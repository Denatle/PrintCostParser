from parser_classes.undetected_parser import __UndetectedParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class coralprintParser(__UndetectedParser):
    def __init__(self, size, counts, proxy):
        self.parsing_page = 'https://www.coral-print.ru/pechat-nakleek/obemnyh/s-logotipom.html'
        super().__init__(size, counts, proxy)

    def parse(self, container: list) -> None:
        self.get(self.parsing_page)

        width = self.wait('width', 30, By.ID)
        height = self.find('height', By.ID)
        count_input = self.find('count', By.ID)

        cut = self.find('slice', By.ID)
        cut = self.to_select(cut)
        cut.select_by_value("1")

        width.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + str(self.size))
        height.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + str(self.size))

        costs = []
        for count in self.counts:
            count_input.clear()
            count_input.send_keys(count)
            cost = self.find('span[id="res"]')
            cost.click()
            sleep(0.2)
            costs.append(int(cost.text))

        container.append(("CORAL", costs))
