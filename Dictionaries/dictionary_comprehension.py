instructor = {
    'name': 'charles',
    'city': 'marvel city',
    'color': 'gold'
}

yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}

parities = {num:('even' if num % 2 == 0 else 'odd') for num in range(1, 100)}