from parsers import yfprint, stolitsaprint, coralprint, gcprint, stickery
import threading


def main():
    parsers = [
        gcprint.gcprintParser(),
        yfprint.yfprintParser(),
        stolitsaprint.stolitsaprintParser(),
        coralprint.coralprintParser(),
        stickery.stickeryParser(),
        ]
    costs = []
    for parser in parsers:
        t = threading.Thread(target=parser.parse, args=[costs])
        t.start()
        t.join()
    print(costs)


if __name__ == "__main__":
    main()
