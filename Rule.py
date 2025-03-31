import re
import random
from colorama import Fore, init

init(autoreset=True)

a = {"destinations": ["Paris", "Goa", "Hawaii", "Iceland"],
     "continents": ["Asia", "Europe", "America"]}
jokes = ["What do call a bear without bees? Ear",
         "Why did the bicycle fall over? Because it was two tired",
         "Why did the scarecrow win an award? Because he was outstanding in his field!"]


def process(b):
    return b.strip().lower()


def greet():
    print("Welcome")
    return input("Who are you? ")


def pref():
    rec = process(input("Enter your preference(destinations/continents)- "))
    if rec in a:
        print("How about", random.choice(a[rec]))
    else:
        print("invalid choice")


def tips():
    days = int(input("How many days will you be staying? "))
    if days > 14:
        print("Try visiting all the landmarks")
    else:
        print("Its going to be hard visiting everything so make a list of your must-visits for a peaceful trip.")


def joke():
    print(random.choice(jokes))


def recomend():
    name = greet()
    print("What would you like, jokes, tips or destinations to visit?")
    while True:
        input1 = process(input("Enter your choice: "))  # Added colon here
        if "tips" in input1:
            tips()
        elif "jokes" in input1:
            joke()
        elif "destinations" in input1:
            pref()
        elif "exit" in input1:
            break
        else:
            print("invalid input")


recomend()