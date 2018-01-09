p1c = input('Enter Player 1\'s choice: ')
p2c = input('Enter Player 2\'s choice: ')

if p1c == p2c:
  print('It\'s a tie!')
elif p1c == 'rock':
  if p2c == 'paper':
    print('Player 2 wins!')
  elif p2c == 'scissors':
    print('Player 1 wins')
elif p1c == 'paper':
  if p2c == 'scissors':
    print('Player 2 wins')
  elif p2c == 'rock':
    print('Player 1 wins')
elif p1c == 'scissors':
  if p2c == 'rock':
    print('Player 2 wins')
  elif p2c == 'paper':
    print('Player 1 wins')
else:
  print('There was an error, try again.')