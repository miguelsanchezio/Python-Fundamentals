from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
  print(f'Player Score: {player_wins} | Computer Score: {computer_wins}')

  player = input('Make your move: ').lower()
  if player == 'quit' or player == 'q':
    break

  rand_num = randint(0, 2)
  if rand_num == 0:
    computer = 'rock'
  elif rand_num == 1:
    computer = 'paper'
  else:
    computer = 'scissors'

  if player == computer:
    print('It\'s a tie!')
  elif player == 'rock':
    if computer == 'paper':
      print(f'Computer wins with {computer}!')
      computer_wins += 1
    else:
      print('Player wins')
      player_wins += 1
  elif player == 'paper':
    if computer == 'scissors':
      print(f'Computer wins with {computer}!')
      computer_wins += 1
    else:
      print('Player wins')
      player_wins += 1
  elif player == 'scissors':
    if computer == 'rock':
      print(f'Computer wins with {computer}!')
      computer_wins += 1
    else:
      print('Player wins')
      player_wins += 1
  else:
    print('There was an error, try again.')

if player_wins > computer_wins:
  print('You win!')
elif player_wins == computer_wins:
  print('It\'s a tie')
else:
  print('The computer won, try again.')

print(f'FINAL SCORE... Player: {player_wins} | Computer: {computer_wins}')