"""File to define Bear class."""

__author__ = "730740774"


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor for Bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases age and hunger when day changes."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Changes hunger based on fish ate."""
        self.hunger_score += num_fish
