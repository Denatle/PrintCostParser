import json


def read_config(file):
    with open(file) as f:
        return json.load(f)
