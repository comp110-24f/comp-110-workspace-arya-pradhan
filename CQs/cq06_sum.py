"""Summing the elements of a list using different loops"""

__author__ = "730740774"


def w_sum(vals: list[float]) -> float:
    """takes input from a list and sums it all up using a while loop"""

    index: int = 0
    total: float = 0.0

    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """takes input from a list and sums it all up using a for loop"""
    total: float = 0.0
    for num in vals:
        total += num
    return total


def f_range_sum(vals: list[float]) -> float:
    """takes input from a list and sums it all up using a for loop and range()"""
    total: float = 0.0
    for num in range(len(vals)):
        total += vals[num]
    return total


print(f_range_sum([1.0, 2.0, 11.5]))
