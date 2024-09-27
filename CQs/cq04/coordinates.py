"""Create a function to make coordinate"""

__author__ = "730740774"


def get_coords(xs: str, ys: str) -> None:
    """Create a function to make cordiates out of strings
    iteraing through each string to make all possibilites"""
    index1: int = 0
    index2: int = 0

    while index1 < len(xs):
        while index2 < len(ys):
            print(f"({xs[index1]}, {ys[index2]})")
            index2 += 1
        # I was doing two print statements before which made me overlap indexs
        index2 = 0
        index1 += 1
