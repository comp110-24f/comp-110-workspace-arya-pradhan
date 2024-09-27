"""Create a function to concatenate"""

__author__ = "730740774"

word1: str = "happy"
word2: str = "tuesday"


def concat(str1: str, str2: str) -> str:
    """Concatenates two strings"""
    return str1 + str2


if __name__ == "__main__":
    print(concat(str1=word1, str2=word2))
