users = [
    {'username': 'samuel', 'tweets':['I love PHP', 'I love Wordpress']},
    {'username': 'katie', 'tweets':['I love HTML', 'I love CSS']},
    {'username': 'jeff', 'tweets':['I love Javascript', 'I love React']},
    {'username': 'bob123', 'tweets':['I love Photoshop', 'I love Illustrator']},
    {'username': 'guitar_dude', 'tweets':['I love Figma']}
]

sorted(users, key=lambda user: user['username'])