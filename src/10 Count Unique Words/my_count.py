import re
import collections


def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = re.findall(r"[0-9a-zA-Z-']+", file.read())
        print(type(text))
        words = list(map(str.lower, text))
        total_count = collections.Counter(words)

    print(f"total: {total_count.total()}")
    print(total_count.most_common(5))


# commands used in solution video for reference
if __name__ == '__main__':
    count_words('./src/10 Count Unique Words/shakespeare.txt')
