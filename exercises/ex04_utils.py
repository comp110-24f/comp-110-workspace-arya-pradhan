""" Creating utility functions """

__author__ = "730740774"


def all(int_list: list[int], num_check: int) -> bool:
    """Function that checks if all the ints in a list are a certain int"""
    # Forgot to take inot account if the len was 0
    if len(int_list) == 0:
        return False

    for num in int_list:
        if num != num_check:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Function that returns the largest int in a list of ints"""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    # Initally set max to 0 but that is unreliable
    max: int = int_list[0]
    for num in int_list:
        if num > max:
            max = num
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function that checks if two int lists are deeply equal"""
    if len(list1) != len(list2):
        return False

    # I tried to use a 'for' loop but found it easier to
    # iterate using a while loop
    index: int = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Concatenates two int lists together, mutating list1 not list2"""
    for num in list2:
        list1.append(num)
