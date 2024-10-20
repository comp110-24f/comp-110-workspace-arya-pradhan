"""Finding a max"""

__author__ = "730740774"


def find_and_remove_max(input_list: list[int]) -> int:
    """returns the larges number in a list and takes it out"""
    if len(input_list) == 0:
        return -1

    max_num: int = input_list[0]
    for num in input_list:
        if num > max_num:
            max_num = num

    # When using a 'for' loop, consecutive 'max_num's would be skipped
    # so I used a while loop for greater control of indexing
    index: int = 0
    while index < len(input_list):
        if input_list[index] == max_num:
            input_list.pop(index)
            index -= 1
        index += 1
    return max_num
