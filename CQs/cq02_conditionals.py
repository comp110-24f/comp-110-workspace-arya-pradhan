"""Creating a simple number guessing game"""

__author__ = "730740774"


def guess_a_number() -> None:
    secret: int = 7
    user_guess: int = int(input("Guess a number: "))
    print(f"Your guess was {user_guess}")

    if user_guess == secret:
        print("You got it!")
    elif user_guess > secret:
        print(f"Your guess was too high! The secret number is {secret}")
    else:
        print(f"Your guess was too low! The secret number is {secret}")
    return None


if __name__ == "__main__":
    guess_a_number()
