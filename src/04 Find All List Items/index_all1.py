def index_all(search_list: list, item):
    res = []
    for n, each in enumerate(search_list):
        if each == item:
            res.append([n])
        elif isinstance(each, list):
            for i in index_all(each, item):
                res.append([n] + i)
    return res

if __name__ == "__main__":
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2)) # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]
