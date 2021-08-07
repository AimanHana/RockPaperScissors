###########Rock Paper Scissors####################
import random
import sys
wins = 0
losses = 0 
ties = 0
move = ''
computer_moves = ['r','p','s']

def replace(name):
  if name == 'r':
    return 'Rock'
  elif name == 's':
    return 'Scissors'
  elif name == 'p':
    return 'Paper'

def end():
  print('Game Over')
  sys.exit()

def start():
  print(f'''
  ##############################################
  #             Game started                   #
  #          ROCK, PAPER, SCISSORS             #
  #     You need 10 points to win the game     #
  ##############################################
''')

def play():
  if wins == 10:
    print('Congratulations, You won the game.')
    end()
  elif losses == 10:
    print('Hard luck, you lost the game')
    end()
  move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit to quit at any time. ')
  computer = random.choice(computer_moves)
  check_move(move,computer)

def check_move(move,computer):
  global wins,losses,ties
  if move == 'q':
    end()
  elif move == computer:
    ties = ties + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('It is a tie')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  elif move =='r' and computer == 's':
    wins = wins + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('You win')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  elif move == 's' and computer == 'p':
    wins = wins + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('You win')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  elif move == 'p' and computer == 'r':
    wins = wins + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('You win')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  elif move == 'r' and computer == 'p':
    losses = losses + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('You lose')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  elif move == 's' and computer == 'r':
    losses = losses + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('You lose')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  elif move == 'p' and computer == 's':
    losses = losses + 1
    print(f'You chose {replace(move)} and the computer chose {replace(computer)}.')
    print('You lose')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    
  else:
    print(f'\'{move}\' is not a valid choice. Please try again.')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
start()
while wins<=10 and losses<=10:
  play()