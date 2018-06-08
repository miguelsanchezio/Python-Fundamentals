import pyfiglet
import requests
import random
from termcolor import colored

game_title = pyfiglet.figlet_format('DAD JOKES!')
colored_game_title = colored(game_title, color='cyan')
print(colored_game_title)

search_term = input('What do you want to hear a joke about? ')

url = 'https://icanhazdadjoke.com/search'

response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': search_term}
)

data = response.json()

if data['total_jokes'] > 0:
    print(f"There are {data['total_jokes']} jokes about \"{search_term}\". Here's one: ")
    ran_num = random.randint(0, data['total_jokes'] - 1)
    print(data['results'][ran_num]['joke'])
else:
    print(f'There aren\'t any jokes about "{search_term}".')