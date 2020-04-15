from csv import DictReader
from random import choice
from termcolor import colored
from bs4 import BeautifulSoup
import requests
import pyfiglet


with open("quotes.csv") as file:
    csv_reader = DictReader(file)
    quotes = list(csv_reader)

url = "http://quotes.toscrape.com"
ascii_title = pyfiglet.figlet_format("Guess The Author")
colored_title = colored(ascii_title, color="yellow")
print(colored_title)


def print_quote(quote):
    print("-----------------------------------")
    print(quote)
    print("-----------------------------------")


def play_game():
    num_guesses = 4
    guess = ""
    random_quote = choice(quotes)
    print_quote(random_quote["Quote"])

    while True:
        if num_guesses > 0:
            guess = input(f"[{colored(num_guesses, color='yellow')} guesses remaining] Who wrote the quote? ")

        if guess == random_quote["Author"] or num_guesses == 0:
            if guess == random_quote["Author"]:
                print("Correct! You win!")
            elif num_guesses == 0:
                print("Game Over.")
                print(f"The answer was: {random_quote['Author']}")
            answer = input("Would you like to play again? (y/n) ")
            while answer != "y" and answer != "n":
                input("Enter a valid input. Would you like to play again? (y/n) ")
            if answer == "y":
                num_guesses = 4
                random_quote = choice(quotes)
                print_quote(random_quote["Quote"])
            elif answer == "n":
                print("Thanks for playing.")
                break
        elif num_guesses > 0:
            num_guesses -= 1
            if num_guesses == 3:
                response = requests.get(url + random_quote["Author URL"])
                soup = BeautifulSoup(response.text, "html.parser")
                birth_date = soup.find(class_="author-born-date").get_text()
                birth_location = soup.find(class_="author-born-location").get_text()
                print(f"Here's a hint: the author was born on {birth_date} {birth_location}.")
            elif num_guesses == 2:
                print(f"Here's a hint: the author's first name starts with {random_quote['Author'][0]}")
            elif num_guesses == 1:
                author_last = random_quote["Author"].split(" ")[1][0]
                print(f"Here's a hint: the author's last name starts with {author_last}")


play_game()
