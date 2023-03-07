from parsers import yfprint, stolitsaprint, coralprint, gcprint, stickery, printraduga
from modules import excel
import threading


def main():
    args = [50, [100, 500, 1000], ""]
    parsers = [
        printraduga.printradugaParser(*args),
        gcprint.gcprintParser(*args),
        # yfprint.yfprintParser(*args),
        stolitsaprint.stolitsaprintParser(*args),
        coralprint.coralprintParser(*args),
        stickery.stickeryParser(*args),
    ]
    costs = []
    for parser in parsers:
        t = threading.Thread(target=parser.parse, args=[costs])
        t.start()
        t.join()

    print(costs)

    indexes = []
    heads = args[1]
    data = []
    for tup in costs:
        indexes.append(tup[0])
        data.append(tup[1])
    excel_ut = excel.excelUtils(indexes, heads, "result.xlsx")
    excel_ut.create_file(data)


if __name__ == "__main__":
    main()
