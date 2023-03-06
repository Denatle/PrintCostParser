from parsers import yfprint, stolitsaprint, coralprint, gcprint, stickery
from parser_classes import main_parser
from modules import excel
import threading


def main():
    args = [50, [100, 500, 1000], ""]
    parsers = [
        # gcprint.gcprintParser(*args),
        # yfprint.yfprintParser(*args),
        # stolitsaprint.stolitsaprintParser(*args),
        # coralprint.coralprintParser(*args),
        stickery.stickeryParser(*args),
    ]
    costs = []
    for parser in parsers:
        t = threading.Thread(target=parser.parse, args=[costs])
        t.start()
        t.join()

    print(costs)

    # indexes = []
    # heads = []
    # for
    # parser = excel.excelWriter()


if __name__ == "__main__":
    main()
