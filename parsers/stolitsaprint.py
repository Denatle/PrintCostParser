from parser_classes.bs4_parser import __bs4Parser


class stolitsaprintParser(__bs4Parser):
    def __init__(self, size, counts, proxy):
        self.parsing_page = "https://stolitsaprint.ru/pechat-nakleek/obemnye/"
        super().__init__(size, counts, proxy)

    def __merge_lists(self, list1, list2):
        return_dict = {}
        for i in range(len(list1)):
            return_dict[list1[i]] = list2[i]
        return return_dict

    def parse(self, container) -> None:
        soup = self.get(self.parsing_page)

        size = self.size / 10
        size = 3.14 * (size / 2) ** 2

        prices1 = []
        prices2 = []

        table = soup.find("tbody")

        row = table.find_all("tr")[1]

        minimum_area = int(row.find_all("td")[1].getText().
                           replace(" ", "").replace("кв.см", "").replace("до", "").replace(",", "."))

        for col in row.find_all("td")[2:]:
            prices1.append(col.getText().replace(" ", "").replace("кв.см", "").replace(",", "."))

        row = table.find_all("tr")[2]

        minimum_costs = list(map(float, row.find_all("td")[1].getText().
                                 replace(" ", "").replace("\xa0руб.", "").replace(",", ".")
                                 .split("руб..нозаказминимумна")))

        for col in row.find_all("td")[2:]:
            prices2.append(col.getText().replace(" ", "").replace("\xa0руб.", "").replace(",", "."))

        costs = self.__merge_lists(list(map(int, prices1)), list(map(float, prices2)))

        f_costs = []

        for count in self.counts:
            area = size * count
            if area < minimum_area:
                cost = max(minimum_costs[1], minimum_costs[0] * area)
            else:
                for count_t, cost_t in costs.items():
                    if area <= count_t:
                        cost = area * cost_t
                        break
                else:
                    cost = area * list(costs.values())[-1]
            f_costs.append(cost)

        container.append(('STOLITSA', f_costs))
