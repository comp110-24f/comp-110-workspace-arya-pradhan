"""Just some dictionary utility functions"""

__author__ = "730740774"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """The keys of the input list becomes the values
    of the output list and vice versa"""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in inverted_dict:
            raise KeyError("Duplicate value detected")
        inverted_dict[input_dict[key]] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns a str which has the most frequent key"""
    # I thought to myself 'I need a way to keep track of a number
    # and coresponding color'
    # and was like oh yeah a dict
    color_count: dict[str, int] = {}

    for key in input_dict:
        if input_dict[key] in color_count:
            # messed up and only put color_count[key]
            color_count[input_dict[key]] += 1
        else:
            color_count[input_dict[key]] = 1

    # finds the max value in color_count
    max_color_count: int = 0
    for key in color_count:
        if color_count[key] > max_color_count:
            max_color_count = color_count[key]

    # returns the first key that has the value of max_color_count
    for key in color_count:
        if color_count[key] == max_color_count:
            return key
    # just in case
    return ""


def count(input_list: list[str]) -> dict[str, int]:
    """returns a dictionary containg how many times a value
    in a list apears in the list"""
    # same logic i used to create color_count{}
    final_dict: dict[str, int] = {}

    for item in input_list:
        if item in final_dict:
            final_dict[item] += 1
        else:
            final_dict[item] = 1
    return final_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """returns a dictionary containing all the words from a list
    that start with the item of the list"""
    # same logic baby
    alpha_dict: dict[str, list[str]] = {}
    for item in input_list:
        # variable mostly for clarity
        first_letter: str = item[0].lower()
        if first_letter in alpha_dict:
            alpha_dict[first_letter].append(item)
        else:
            alpha_dict[first_letter] = [item]
    return alpha_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    # same
    # logic
    # baby
    if day in input_dict:
        # forgot to take into account multiple students
        if student not in input_dict[day]:
            input_dict[day].append(student)
    else:
        input_dict[day] = [student]
