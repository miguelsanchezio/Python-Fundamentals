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

num_jokes = data['total_jokes']

if num_jokes > 1:
    print(f"There are {num_jokes} jokes about \"{search_term}\". Here's one: ")
    ran_num = random.randint(0, num_jokes - 1)
    print(data['results'][ran_num]['joke'])
elif num_jokes == 1:
    print(f'There\'s one joke about "{search_term}".')
    print(data['results'][0]['joke'])
else:
    print(f'There aren\'t any jokes about "{search_term}".')