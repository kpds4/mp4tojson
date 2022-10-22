import json


def read_json(file_name):
    with open(file_name) as f:
        data = json.load(f)

    print(data)


if __name__ == "__main__":
    read_json(file_name="_1uqL32ASRE.mp4.json")