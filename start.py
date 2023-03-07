from parsers import yfprint, stolitsaprint, coralprint, gcprint, stickery, printraduga
from modules import excel, config
import threading


def main():
    cf = config.read_config("config.json")
    args = [cf["size"], cf["count"], cf["proxy"]]
    parsers = [
        printraduga.printradugaParser(*args),
        gcprint.gcprintParser(*args) if not cf["disable_gc"] else None,
        yfprint.yfprintParser(*args) if not cf["disable_yf"] else None,
        stolitsaprint.stolitsaprintParser(*args) if not cf["disable_stolitsa"] else None,
        coralprint.coralprintParser(*args) if not cf["disable_coral"] else None,
        stickery.stickeryParser(*args) if not cf["disable_stickery"] else None,
    ]
    costs = []
    for parser in parsers:
        if not parser:
            continue
        try:
            t = threading.Thread(target=parser.parse, args=[costs])
            t.start()
            t.join()
        except Exception as e:
            print(f"Возникла ошибка: {e}, в процессе парсинга {parser}")
        parser.quit()

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
