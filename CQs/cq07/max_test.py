"""Testing for find_max"""

__author__ = "730740774"


from find_max import find_and_remove_max


def test_find_and_remove_max_edge_case() -> None:
    """Checks edge case if find_and_remove returns -1 since empty list"""
    assert find_and_remove_max([]) == -1


def test_find_and_remove_max_use_case() -> None:
    """Checks if find_and_remove returns 4"""
    test: list[int] = [3, 4, 4, 2, 1]
    assert find_and_remove_max(test) == 4


def test_find_and_remove_max_mutate_use_case() -> None:
    """Checks if find_and_remove mutates test"""
    test: list[int] = [3, 4, 4, 2, 1]
    find_and_remove_max(test)
    assert test == [3, 2, 1]
