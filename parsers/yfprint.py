from parser_classes.selenium_parser import __SeleniumParser


class yfprintParser(__SeleniumParser):
    def __init__(self) -> None:
        self.parsing_page = "https://www.yfprint.ru/polygrafiya/izgotovlenie-nakleek-so-smoloj/"
        super().__init__()

    def parse(self, container) -> None:
        self.get(self.parsing_page)

        self.wait("input[id='p0v0']").click()

        self.find("input[id='p1v4']").click()

        text_fields = self.find_all("input[class='a_textfield']")
        width = text_fields[1]
        height = text_fields[2]
        width.clear()
        height.clear()
        width.send_keys(self.size)
        height.send_keys(self.size)

        self.find("input[id='p2v3']").click()

        self.find("input[id='p3v0']").click()

        self.find("input[id='p4v0']").click()

        self.find("input[id='p5v0']").click()

        material = self.find("select[class='a_calcdata a_colorselector']")
        material = self.to_select(material)
        material.select_by_value("5")

        button = self.find("button[class='btn-default']")

        count_input = self.find("input[class='a_textfield wide a_calcdata']")

        costs = []
        for count in self.counts:
            count_input.clear()
            count_input.send_keys(count)
            button.click()
            cost = int(self.wait("span[class='a_result']").text.replace(" руб.", ""))
            while cost in costs:
                cost = int(self.find("span[class='a_result']").text.replace(" руб.", ""))

            costs.append(cost)

        container.append(('YF', costs))
