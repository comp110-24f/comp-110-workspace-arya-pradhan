"""Ex03 - Making Wordle"""

__author__ = "730740774"


def main(secret: str) -> None:
    """The entrypoint of the program and manages the flow of the game"""
    counter: int = 1

    while counter <= 6:
        print(f"=== Turn {counter}/6 ===")
        # At first I tried to put run it all on one line
        # but then I was unable to check if I won earlier than 6 guesses
        # so I broke it down to check 'user' and 'secret'
        user: str = input_guess(secret_word_len=len(secret))
        print(emojified(secret_word=secret, user_guess=user))

        if user == secret:
            print(f"You won in {counter}/6 turns!")
            counter = 10

        counter += 1

    if counter == 7:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Asks user to input a x length word and loops until given a fitting str"""
    guess: str = str(input(f"Enter a {secret_word_len} character word: "))
    guess_len: int = len(guess)

    while secret_word_len != guess_len:
        guess = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
        guess_len = len(guess)
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks each index if secret_word contains char_guess"""
    assert len(char_guess) == 1
    index: int = 0

    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Display the results of a guess as emojis"""
    assert len(user_guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # At first I just printed each box but that would make it different
    # levels, so I just made another variable and added it there
    final: str = ""
    index: int = 0

    while index < len(user_guess):
        # The way we coded contains_char, I knew I wanted to split 'if' statements
        # by white vs (green and yellow) then doing green vs yellow
        if contains_char(secret_word=secret_word, char_guess=user_guess[index]):
            if user_guess[index] == secret_word[index]:
                final += GREEN_BOX
            else:
                final += YELLOW_BOX
            index += 1
        else:
            final += WHITE_BOX
            index += 1
    return final


if __name__ == "__main__":
    main(secret="codes")
