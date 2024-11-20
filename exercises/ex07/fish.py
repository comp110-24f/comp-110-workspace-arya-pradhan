"""File to define Fish class."""

__author__ = "730740774"


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Constructor for fish."""
        self.age = 0
        return None

    def one_day(self):
        """Increases the age of fish when day changes."""
        self.age += 1
        return None
