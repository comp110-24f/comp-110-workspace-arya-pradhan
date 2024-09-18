"""Iterating over a string using while loop"""

__author__ = "730740774"


# Commented out code used for testing
def num_instances(phrase: str, search_char: str) -> int:
    charCount: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            charCount += 1
        #            print("+1")
        #        else:
        #            print("nothing")
        index += 1
    #    print(charCount)
    return charCount
