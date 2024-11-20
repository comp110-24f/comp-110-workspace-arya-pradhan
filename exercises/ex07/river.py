"""File to define River class."""

__author__ = "730740774"


from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes the fish and bears that are too old."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)

        new_bear: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bear.append(bear)
        self.fish = new_fish
        self.bears = new_bear

        return None

    def remove_fish(self, amount: int) -> None:
        """Removes a certain amount of fish."""
        for fish in range(amount):
            self.fish.pop(0)

    def bears_eating(self):
        """Feed the bears in order until not enough fish."""
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)
        return None

    def check_hunger(self):
        """Removes the starving bears."""
        new_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bear.append(bear)
        self.bears = new_bear
        return None

    def repopulate_fish(self):
        """Repopulate the fish by (n//2)*4."""
        for fish in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulate the bears by n//2."""
        for bear in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """View the river stats."""
        # forgot to make it len()
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week of river activities."""
        # tried to use for loop but didn't work so forced it
        # not like the amount of days in a week will change
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
