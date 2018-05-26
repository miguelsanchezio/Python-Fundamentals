from random import randint

rand_num = randint(0, 2)

if rand_num == 0:
  computer = 'rock'
elif rand_num == 1:
  computer = 'paper'
else:
  computer = 'scissors'

player = input('Make your move: ').lower()

if player == computer:
  print('It\'s a tie!')
elif player == 'rock':
  if computer == 'paper':
    print(f'Computer wins with {computer}!')
  else:
    print('Player wins')
elif player == 'paper':
  if computer == 'scissors':
    print(f'Computer wins with {computer}!')
  else:
    print('Player wins')
elif player == 'scissors':
  if computer == 'rock':
    print(f'Computer wins with {computer}!')
  else:
    print('Player wins')
else:
  print('There was an error, try again.')