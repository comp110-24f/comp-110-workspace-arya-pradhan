""" Mutating Function """

__author__ = "730740774"


def manual_append(input_list: list[int], num: int) -> None:
    """Function to manualy append"""
    input_list.append(num)


def double(input_list: list[int]) -> None:
    """Function to double each index of a list"""
    index: int = 0
    while index < len(input_list):
        input_list[index] = input_list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

# I think both print statements will be [2,4,6]
print(list_1)
print(list_2)
