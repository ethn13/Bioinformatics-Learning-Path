# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
# Define globals
secret_number = 0
remaining_guesses = 0
"""
mode:
    0 means range is 0-100
    1 means range is 0-1000
"""
mode = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses, mode
    if(mode == 0):
        secret_number = random.randrange(0, 100)
        remaining_guesses = int(math.ceil(math.log(100, 2)))
        print "New game. " + "Range is[0, 100)"
        print "Number of remaining guesses is " + str(remaining_guesses)
        print ""
    else:
        secret_number = random.randrange(0, 1000)
        remaining_guesses = int(math.ceil(math.log(1000, 2)))
        print "New game. " + "Range is [0, 1000)"
        print "Number of remaining guesses is " + str(remaining_guesses)
        print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global mode
    mode = 0
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global mode
    mode = 1
    new_game()
    
def input_guess(guess):
    global remaining_guesses
    remaining_guesses -= 1
    print "Guess was " + guess
    print "Number of remaining guesses is " + str(remaining_guesses)
    # main game logic goes here	
    guess = int(guess)
    if(guess == secret_number):
        print "Correct!"
        print ""
        new_game()
    elif(remaining_guesses == 0):
        print "You ran out of guesses.  The number was " + str(secret_number)
        print ""
        new_game()
    elif(guess > secret_number):
        print "Lower!"
        print ""
    else:
        print "Higher!"
        print ""
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Guess a number: ", input_guess, 50)
frame.add_button("Range: [0, 100)",range100)
frame.add_button("Range: [0, 1000)",range1000)
frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
