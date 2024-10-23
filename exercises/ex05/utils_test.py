"""unit tests for utils"""

__author__ = "730740774"

import pytest
from utils import only_evens, sub, add_at_index


def test_only_evens_return() -> None:
    """Test if only_evens returns expected value"""
    assert only_evens(input_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]


def test_only_evens_mutate() -> None:
    """Test if only_evens mutates input_list"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    only_evens(input_list=test_list)
    assert test_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_only_evens_edge() -> None:
    """Test if only_evens returns an empty list when given empty list"""
    assert only_evens(input_list=[]) == []


def test_sub_return() -> None:
    """Test if sub returns expected value"""
    test_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(input_list=test_list, start=4, end=8) == [4, 5, 6, 7]


def test_sub_mutate() -> None:
    """Test if sub mutates input_list"""
    test_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub(input_list=test_list, start=4, end=8)
    assert test_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sub_edge() -> None:
    """Test if sub returns an empty list when given an empty list"""
    assert sub(input_list=[], start=3, end=6) == []


def test_add_at_index_return() -> None:
    """Test if add_at_index mutates an expected value"""
    test_list: list[int] = [0, 1, 2, 3]
    add_at_index(input_list=test_list, new_element=99, given_index=2)
    assert test_list == [0, 1, 99, 2, 3]


def test_add_at_index_mutate() -> None:
    """Test if add_at_index mutates input_list"""
    test_list: list[int] = [0, 1, 2, 3]
    add_at_index(input_list=test_list, new_element=99, given_index=2)
    assert test_list != [0, 1, 2, 3]


def test_add_at_index_edge() -> None:
    """Test that add_at_index raises an IndexError for an invalid index"""
    test_list: list[int] = [0, 1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(input_list=test_list, new_element=99, given_index=20)
