"""EX-2 - Chardle - Making a bootleg, and ultimately less fun, Wordle"""

__author__ = "730740774"


def main() -> None:
    contains_char(hidden_word=input_word(), user_guess=input_letter())


def input_word() -> str:
    user_word: str = str(input("Enter a 5-character word: "))
    # Instead of creating a nested 'if' statement I use the 'or' operator
    if len(user_word) < 5 or len(user_word) > 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word


def input_letter() -> str:
    user_letter: str = str(input("Enter a single character: "))
    # Instead of creating a nested 'if' statement I use the 'or' operator
    if len(user_letter) < 1 or len(user_letter) > 1:
        print("Error: Character must be a single character.")
        exit()
    return user_letter


def contains_char(hidden_word: str, user_guess: str) -> None:
    count: int = 0
    print(f"Searching for {user_guess} in {hidden_word}")
    if hidden_word[0] == user_guess:
        print(f"{user_guess} found at index 0")
        count += 1

    if hidden_word[1] == user_guess:
        print(f"{user_guess} found at index 1")
        count += 1

    if hidden_word[2] == user_guess:
        print(f"{user_guess} found at index 2")
        count += 1

    if hidden_word[3] == user_guess:
        print(f"{user_guess} found at index 3")
        count += 1

    if hidden_word[4] == user_guess:
        print(f"{user_guess} found at index 4")
        count += 1

    if count == 0:
        print(f"No instances of {user_guess} found in {hidden_word}")
    else:
        print(f"{count} instances of {user_guess} found in {hidden_word}")


if __name__ == "__main__":
    main()
