# Interactive rock-paper-scissors-lizard-spock game.
import random

def name_to_number(name):
	if name == 'rock':
		return 0
	elif name == 'spock':
		return 1
	elif name == 'paper':
		return 2
	elif name == 'lizard':
		return 3
	elif name == 'scissors':
		return 4
	else:
		print('Please enter one of the following options: rock, spock, paper, lizard, scissors')

def number_to_name(number):
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'spock'
	elif number == 2:
		return 'paper'
	elif number == 3:
		return 'lizard'
	elif number == 4:
		return 'scissors'
	else: 
		print('Please enter a number between 0 and 4')

def rpsls(player_choice):
    print()
    print('Player chooses '+ player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(1,5,1)
    comp_choice=number_to_name(comp_number)
    print()
    print('Computer chooses ' + comp_choice)
    difference=player_number - comp_number
    print()
    
    if (difference % 5 == 1) or (difference % 5 == 2) :
        print('Player Wins!')
    elif (difference % 5 == 3) or (difference % 5 == 4):
        print('Computer Wins!')
    else:
        print("Player and Computer tie!")
    restart()


def restart():
	print()
	print("Would you like to play again? Enter Y or N.")
	an=input()
	if an == 'Y' or an == 'y':
		print('Welcome!Please enter one of following: rock, paper, scissors, lizard, spock')
		name=input()
		rpsls(name.lower())
	elif an == 'N' or an =='n':
		print('Good bye!')
		exit
	else:
		print('Please enter Y or N')
        
print('Welcome!Please enter one of following: rock, paper, scissors, lizard, spock')       
name=input()
rpsls(name.lower())



