p1c = input('Enter Player 1\'s choice: ')
p2c = input('Enter Player 2\'s choice: ')

if p1c == 'rock' and p2c == 'paper':
  print('Player 2 wins!')
elif p1c == 'rock' and p2c == 'scissors':
  print('Player 1 wins')
elif p1c == 'paper' and p2c == 'scissors':
  print('Player 2 wins')
elif p1c == 'paper' and p2c == 'rock':
  print('Player 1 wins')
elif p1c == 'scissors' and p2c == 'rock':
  print('Player 2 wins')  
elif p1c == 'scissors' and p2c == 'paper':
  print('Player 1 wins')