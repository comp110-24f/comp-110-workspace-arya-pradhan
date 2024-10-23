"""Creating utility functins"""

__author__ = "730740774"


def only_evens(input_list: list[int]) -> list[int]:
    """From a given list returns only the even numbers in a new list"""
    even_list: list[int] = []
    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Generate a list which is a subset of the input list based on parameters"""
    sub_list: list[int] = []
    index: int = 0
    while index < len(input_list):
        if index >= start and index < end:
            sub_list.append(input_list[index])
        index += 1
    return sub_list


def add_at_index(input_list: list[int], new_element: int, given_index: int) -> None:
    """Modify the input list to place the element at given indx"""
    if given_index < 0 or given_index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    append_list: list[int] = []
    temp: int = 0

    # Indexing was weird in a traditional loop and instead
    # I just pop'd out all the elements from the given_index
    # and made a sperate list then just appended what I needed
    # Also I didn't read the hint till I was done

    for num in range(len(input_list) - given_index):
        temp = input_list.pop(given_index)
        append_list.append(temp)
    input_list.append(new_element)
    for num in append_list:
        input_list.append(num)
