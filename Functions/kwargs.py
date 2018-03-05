def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f'{person}\'s favorite color is {color}')

fav_colors(miguel='red', steph='blue', grant='yellow')

def special_greeting(**kwargs):
    if 'David' in kwargs in kwargs['David'] == 'special':
        return 'You get a special greeting David!'
    elif 'David' in kwargs:
        return f'{kwargs["David"]} David!'

    return 'New phone who dis?'

print(special_greeting(Heather='hello', David='special'))