from parser_classes.bs4_parser import __bs4Parser


class stickeryParser(__bs4Parser):
    def __init__(self, size, counts, proxy):
        self.parsing_page = "https://www.stickery.ru/produktsiya/nakleyki/obemnye-nakleiki/"
        super().__init__(size, counts, proxy)

    def __merge_lists(self, list1, list2):
        return_dict = {}
        for i in range(len(list1)):
            return_dict[list1[i]] = list2[i]
        return return_dict

    def __get_numbers(self, element):
        return_text = element.getText().replace("до ", "").replace("от ", "").replace(" кв.см.", "")
        return float(return_text)

    def parse(self, container) -> None:
        soup = self.get(self.parsing_page)

        size = self.size / 10
        size = 3.14 * (size / 2) ** 2

        table = soup.find("tbody")
        minimum_cost = soup.find_all("p")
        minimum_cost = float(minimum_cost[3].getText().replace("*минимальная сумма заказа =", "").replace(" руб.", ""))

        rows = table.find_all("tr")

        costs = []

        for row in rows[2:]:
            cols = row.find_all("td")
            if size > self.__get_numbers(cols[0]):
                continue
            costs = list(map(self.__get_numbers, cols[1:]))
            break
        else:
            costs = list(map(self.__get_numbers, rows[-1].find_all("td")[1:]))
        costs = self.__merge_lists(list(map(self.__get_numbers, rows[1].find_all("td"))), costs)

        (max_cost := next(iter(costs)), costs.pop(max_cost))

        f_costs = []
        for count in self.counts:
            if count < list(costs.keys())[-1]:
                cost = max(minimum_cost, size * count * list(costs.values())[-1])
                f_costs.append(cost)
                continue
            for i in range(len(list(costs.keys())) - 1):
                if list(costs.keys())[i + 1] <= count:
                    cost = max(minimum_cost, size * count * list(costs.values())[i])
                    break
            else:
                cost = max(minimum_cost, size * count * max_cost)
            f_costs.append(cost)
        container.append(('STICKERY', f_costs))
