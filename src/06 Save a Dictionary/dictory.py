import json


def save_dict(input_dict: dict, file_path):
    with open(file_path, "w") as f:
        json.dump(input_dict, f)


def load_dict(file_path):
    with open(file_path, "r") as f:
        res = json.load(f)
    return res


if __name__ == '__main__':
    save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
    print(load_dict('test.pickle'))
    # {1: 'a', 2: 'b', 3: 'c'}
