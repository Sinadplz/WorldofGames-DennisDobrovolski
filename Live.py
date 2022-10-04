global difficulty, selection
import GuessGame
import MemoryGame
import CurrencyRouletteGame
from score import add_score


def welcome(name):
    name = input("Greetings! What is your name?\n")
    print(f"Welcome {name} to the World of Games! \nHere you can find many cool games to play!\n")
    return name


def load_game():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    2. Guess Game - guess a number and see if you chose like the computer")
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    while True:
        try:
            decision = int(input("Please insert a number between 1 - 3: "))
            while 3 < decision or decision < 1:
                decision = int(input("Please insert a number between 1 - 3: "))
            difficulty = int(input('Please choose game difficulty from 1 to 5:'))
            while 5 < difficulty or difficulty < 1:
                difficulty = int(input("Please insert a number between 1 - 5: "))

        except ValueError:
            print("Error: Please enter numbers only.")
            continue
        if decision == 1:
            GuessGame.play(difficulty)
            if bool(GuessGame) is True:
                add_score(difficulty=difficulty)
        if decision == 2:
            MemoryGame.play(difficulty)
            if bool(MemoryGame) is True:
                add_score(difficulty=difficulty)
        if decision == 3:
            CurrencyRouletteGame.play(difficulty)
            if bool(CurrencyRouletteGame) is True:
                add_score(difficulty=difficulty)
        return difficulty, decision
