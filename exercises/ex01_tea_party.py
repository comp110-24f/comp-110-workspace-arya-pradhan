"""Calculate the logistics of a tea party based on the number of guests"""

__author__: str = "730740774"


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    # I was thinking of how to call cost w/o any variables
    # then realized I can call a function as an arguement
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    """Return the amount of tea bags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """Retrun the number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the cost of the tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
