from wordle import Wordle
from colorama import Fore

def main():
    print("hello")
    wordle = Wordle("messi")

    while wordle.can_attempt:
        x = input("type your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} characters long!!"
                + Fore.RESET
            )
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")
        
    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle")

if __name__ == "__main__":
    main()