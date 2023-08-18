import re

def is_palindrome(phrase: str) -> bool:
    first = "".join(re.findall(r"[a-z]", phrase.lower()))
    back = first[::-1]
    return first == back

if __name__ == "__main__":
    print(is_palindrome('hello world'))
    print(is_palindrome('Go hang, a salami, I"m a lasagna hog.'))
