# You can find the game at the URL below:
#http://www.codeskulptor.org/#user42_fljLAnVqNU_11.py

#"Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random

limit=100
message='Hello! Welcome!'
# helper function to start and restart the game
def new_game():
    global limit
    if limit == 100:
        range100()
    else:
        range1000()
    

# define event handlers for control panel
def range100():
    """button that changes the range to [0,100] and starts a new game"""
    global secret_number, max_guess, limit
    limit=100
    max_guess=7
    secret_number=random.randrange(0, limit)
    print'A new game begins, your range is 0-100.\nYou have', max_guess,'guesses remaining.\n'
    return max_guess


def range1000():
    """button that changes the range to [0,1000] and starts a new game"""    
    global secret_number, max_guess, limit
    limit = 1000
    max_guess = 10
    secret_number=random.randrange(0, limit)
    print'A new game begins, your range is 0-1000.\nYou have', max_guess,'guesses remaining.\n'
    return max_guess
    
def input_guess(guess):
    try:
        global max_guess
        guess=int(guess)
        max_guess -= 1
        print
        print 'Guess was', guess
        error_check(guess) 
        
                    
        if guess == secret_number:
            print 'Correct!! You won! Play again!\n'
            new_game() 
            
        elif max_guess == 0:
            print 'Sorry, you lost. The secret number was',secret_number,'\nTry again!\n'
            new_game()
            
        elif guess > secret_number:
            print 'Guess lower. You have', max_guess,'guesses remaining.\n'
            
        elif guess < secret_number:
            print 'Guess higher. You have', max_guess,'guesses remaining.\n'
    
    except ValueError:
        """except clause catches ValueError/if user enters letters instead of integers"""
        print
        print 'Oops!, you entered "',guess,'"\nPlease enter an integer.'
       
              
def error_check(guess):
    """checks to see if guess is within range"""
    if limit == 100:
        if guess < 0 or guess > 100: 
            print 'Oops! Please enter a number within range.'
    elif limit == 1000:
        if guess < 0 or guess > 1000: 
            print 'Oops! Please enter a number within range.'
           
def draw(canvas):
    canvas.draw_text(message, [5,110], 28, "Red")   

    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0-100]", range100, 200)
frame.add_button("Range is [0-1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.set_draw_handler(draw)

# call new_game 
print 'Welcome to Guess the Number:\n [Guess the secret number within the given range]\n [You can also change the range and start\n a new game by clicking on a range button]\n'
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
