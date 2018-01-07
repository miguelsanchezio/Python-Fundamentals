# conditional statements
# if some condition is True:
#   do something
# elif some other condition is True:
#   do something
# else:
#   do something

name = 'Grant'

if name == 'Ash Ketchup':
  print('Pokemon')
elif name == 'Goku':
  print('Dragonball')
else:
  print('10X')

# comparison operators
1 == 1 # True
1 != 1 # False
1 < 2 # True
1 > 2 # False
1 <= 1 # True
1 >= 2 # False

# logical operators
age = 6

if age > 2 and age < 8:
  print('Child price.')

city = input('Where do you live? ')
if city == 'los angeles' or city == 'san francisco':
  print('You live in California.')
else:
  print('You don\'t live in California')

age = 21
if not((age >= 2 and age <= 8) or age >= 65):
  print('You are not a child or senior. You pay 10 dollars.')
else:
  print('You are a child or senior.')
