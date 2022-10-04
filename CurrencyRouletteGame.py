import urllib.request as r
import json
import random
import os


def currency(difficulty):
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=2e015e19466c486dc19f"
    response = r.urlopen(url)
    data = json.load(response)
    ex = int(data["USD_ILS"])
    usd = int(random.uniform(1, 100))
    t = usd * ex
    low = int(t - (5 - difficulty))
    high = int(t + (5 - difficulty))
    return usd, t, low, high


def user_guess(usd):
    while True:
        try:
            guess = int(input(f"What's {usd}$ in ILS: "))
        except ValueError:
            print("Please enter numbers only")
            continue
        return guess


def play(difficulty):
    usd, t, low, high = currency(difficulty)
    guess = user_guess(usd)
    os.system('cls' if os.name == 'nt' else 'clear')
    if high >= guess >= low:
        return True
    else:
        return False
