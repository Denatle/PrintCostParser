from parser_classes.selenium_parser import __SeleniumParser
from time import sleep


class gcprintParser(__SeleniumParser):
    def __init__(self):
        self.parsing_page = "https://gcprint.ru/catalog/nakleyki/stikery-s-zalivkoy-smoloy/?utm_medium=cpc&utm_source=yandex&utm_campaign=pechat_nakleek_poisk_vch&utm_content=%7cc%3a47196033%7cg%3a4009760574%7cb%3a8220214298%7ck%3a18754346939%7cst%3asearch%7ca%3ano%7cs%3anone%7ct%3apremium%7cp%3a3%7cr%3a%7cdev%3adesktop&utm_term=..ob..emnie_nakleyki..&cm_id=47196033_4009760574_8220214298_18754346939__none_search_type1_no_desktop_premium_213&_openstat=zglyzwn0lnlhbmrlec5ydts0nze5njazmzs4mjiwmje0mjk4o3lhbmrlec5ydtpwcmvtaxvt&yclid=4970564170182076720"
        super().__init__()

    def parse(self, container) -> None:
        self.get(self.parsing_page)

        width = self.wait('input[name="WIDTH"]')
        height = self.find('input[name="HEIGHT"]')
        count_input = self.find('input[name="COUNT"]')

        width.clear()
        width.send_keys(self.size)
        height.clear()
        height.send_keys(self.size)

        button = self.find('p[class="g-button g-button_green holst-calc__submit js-submit"]')

        costs = []
        for count in self.counts:
            count_input.clear()
            count_input.send_keys(count)
            button.click()
            sleep(0.4)
            cost = self.find('span[class="js-result-sum-long"]')
            costs.append(int(cost.text))
        container.append(('GC', costs))
