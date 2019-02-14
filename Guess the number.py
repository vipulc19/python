# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    secret_number = 0
    rem = 0
    num_range = 0

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print("\nNew game. Range is from 0 to 100")
    new_game()
    global secret_number, rem, num_range
    secret_number = random.randrange(0,100)
    rem = 7
    num_range =  100
    print("No. of remaining guesses is ",rem)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print("\nNew game. Range is from 0 to 1000")
    new_game()
    global secret_number, rem, num_range
    secret_number = random.randrange(0,1000)
    rem = 10
    num_range = 1000
    print("No. of remaining guesses is ",rem)

def input_guess(guess):
    # main game logic goes here	
    print()
    global secret_number, rem
    num = int(guess)
    rem -=1
    print("Guess was ",num)
    print("No. of remaining guesses is ",rem)
    if(num == secret_number):
        print("Correct!")
        if(num_range == 100):
            range100()
        else:
            range1000()
        return
    
    if(rem == 0):
        print("You ran out of guesses. The number was ",secret_number)
        if(num_range == 100):
            range100()
        else:
            range1000()
        return 
    
    if(num > secret_number):
        print("Lower!")
    elif(num < secret_number):
        print("Higher!")
         
    
# create frame
frame = simplegui.create_frame("Guess",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,100)
frame.add_button("Range is [0,1000)",range1000,100)
frame.add_input("Enter guess:",input_guess,100)
frame.start()
# call new_game 
new_game()
range100()

# always remember to check your completed program against the grading rubric
