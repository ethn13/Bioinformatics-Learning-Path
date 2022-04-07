# Rock-paper-scissors-lizard-Spock template
import simplegui

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if(name == "rock"): return 0
    elif(name == "Spock"): return 1
    elif(name == "paper"): return 2
    elif(name == "lizard"): return 3
    elif(name == "scissors"): return 4
    else:
        print "Error: Invalid weapon name"
        return 


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if(number == 0): return "rock"
    elif(number == 1): return "Spock"
    elif(number == 2): return "paper"
    elif(number == 3): return "lizard"
    elif(number == 4): return "scissors"
    else:
        print "Error: Invalid number to convert to a type of weapon"
    
import random
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    #If player enter a invalid choice then end the function immediately
    if(name_to_number(player_choice) == None):
        print "The game is unable to continue because of the invalid player choice\n"
        return
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if(result == 0):
        print "Player and computer tie!"
    elif(result <= 2):
        print "Computer wins!"
    else:
        print "Player wins!"
    # print a blank line to separate consecutive games
    print ""

# Event handlers
def play_game(player_choice):
    rpsls(player_choice)

# Create frame and register event handlers
frame = simplegui.create_frame("RPSLS", 200, 200)
frame.add_input("Enter player choice: ", play_game, 100)

# Start frame
frame.start()
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


