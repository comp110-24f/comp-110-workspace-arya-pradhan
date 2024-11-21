"""Continuation of linked_list from class."""

from __future__ import annotations

__author__ = "730740774"


class Node:
    """Class for Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Constructor."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Shows linked list as a str."""
        rest: str = ""
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)

        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the .value of a Node at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:
        # forgot to check if index was 0 and ran into some errors
        return head.value
    else:
        return value_at(head=head.next, index=index - 1)
        # forgot to subtract index by 1


def max(head: Node | None) -> int:
    """Returns the Node that has the max value."""
    if head is None:
        raise ValueError("Cannot call max with None")

    if head.next is None:
        return head.value

    # felt easier to set the recurssion before going into the if statements
    current_max: int = max(head=head.next)

    if head.value > current_max:
        return head.value
    else:
        return current_max


def linkify(items: list[int]) -> Node | None:
    """Turns a list[int] into a linked list of Nodes."""
    if items == []:
        return None
    else:
        # was running into errors but turns out I wasn't splicing correctly
        rest: Node = Node(items[0], linkify(items=items[1:]))
        return rest


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies each item by the factor and create a new linked list."""
    if head is None:
        return None
    else:
        rest: Node = Node(
            value=head.value * factor, next=scale(head=head.next, factor=factor)
        )
    return rest
