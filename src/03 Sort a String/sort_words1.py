

def sort_words(phrase: str):
    return " ".join(sorted(phrase.split(" "), key=lambda x: x.lower()))


if __name__ == "__main__":
    print(sort_words('banana ORANGE apple'))
    print(sort_words('string of words'))
