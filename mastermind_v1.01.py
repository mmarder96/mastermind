### Created by Max Marder, Sam Nguon, Michelle Niland on 1/30/18

##############
#   IMPORTS  #
##############

# import module for title and information long strings
import game_text as txt

import random
import sys
import re
from itertools import product

################
#   VARIABLES  #
################

#---SECRET CODE---#
secret_code = ''

#---GAME PEGS---#

# possible secret code colors
color_pegs = ["R", "G", "B", "Y", "O", "P"]

# possible returned code colors
return_pegs = ['X','O','-']

#---GAME MODE SETTINGS---#

# change the setting to turn the game on/off
game_on = True

# change the setting to True to select mode
user_mode = False
comp_mode = False

# user mode difficulties
difficulties = {'E':25, 'M':15, 'H':5}

# switch difficulties
game_difficulty = ''

# user stats
tries = 0
hint_count = 0
score = 0

#---SPECIAL COMMANDS---#

special_commands = ['HELP', 'QUIT', 'HINT']

################
#   FUNCTIONS  #
################

#---SELECT GAME MODE---#
## Created by: Max
def select_game_mode():
    
    global user_mode
    global comp_mode
    
    # print instructions for game mode selection
    print (txt.game_mode_instr)
    
    # prompt user to select their game mode
    while (not user_mode and not comp_mode):
        game_mode = input("Please select your game mode [u/c]: ").upper()
        # select user mode
        if game_mode == 'U':
            init_user_mode()
        # select computer mode
        elif game_mode == 'C':
            # turn on comp mode loop
            init_comp_mode()
        else:
            print("Please enter 'u' for user mode or 'c' for comp mode!")
            
#---INITIALIZE USER MODE---#
## Created by: Max
def init_user_mode():
    
    global secret_code
    global user_mode
    
    # print user mode instructions
    print(txt.user_mode_instr)
    # choose difficulty
    select_difficulty()
    
    # generate random secret code for the user to guess
    gen_secret_code()

    # turn on user mode loop
    user_mode = True
 
#---PROMPT USER DIFFICULTY---#
## Created by: Michelle
def select_difficulty():
    
    global game_difficulty
    
    while (game_difficulty not in difficulties.keys()):
        game_difficulty = input("Please select your game difficulty [e/m/h]: ").upper()

#---GENERATE SECRET CODE---#
# generates and returns a secret code to be used in the user mode
## Created by: Max
def gen_secret_code():
    
    global secret_code
    
    secret_array = random.sample(color_pegs, 4)
    secret_code = ''.join(secret_array)

#---GUESS INPUT---#
## Created by: Michelle
def user_guess_prompt():
    
    # display try count
    print("\nTry:", tries+1)
    # prompt user to enter their guess
    user_guess = input("Enter your guess: ").upper()
    
    # reformat the user's guess
    user_guess = user_guess_format(user_guess)
    
    # return the user's reformatted guess to the user mode loop
    return user_guess

#---GUESS FORMATTING---#
### Created by Michelle
# checks if the user formatted their guess correctly
def user_guess_format(user_guess):
    
    # set to false if user uses incorrect format
    correct_format = True
    
    #sanitize input, remove any seperator chars and rejoin
    user_guess = re.split("[., \-!?$@#*+-;<>:%^&]+", user_guess)
    user_guess= "".join(user_guess)     
      
    # check if user typed HINT or QUIT
    if user_guess == "QUIT":
        quit_game()
    elif user_guess == "HINT":
        user_hint()
    elif user_guess =="HELP":
        user_help()
        
    # make sure the user's guess is the correct length
    elif len(user_guess) != len(secret_code):
        print("Please enter", len(secret_code), "colors.")
        correct_format = False

    # check if user used correct colors in their code
    elif any(c not in color_pegs for c in user_guess): 
        print ("Please only use the following colors:", color_pegs)
        correct_format = False  
        
    # if user doesn't use the correct format reprompt them
    if correct_format == False:
       user_guess = user_guess_prompt() 
    
    # return the reformatted user guess
    return user_guess
 
#---QUIT HANDLING---#
# checks if the user really wants to quit
## Created by: Max
def quit_game():
    
    # bring global game state into the functional namespace
    global game_on
    global user_mode
    global comp_mode
    
    # prompt the user to confirm quitting
    quit_confirm = input("\nAre you sure you want to quit [y/n]: ").upper()
    if quit_confirm =="N":
         print ("\nGreat! Let's keep playing!")
    elif quit_confirm == "Y":
               
        # reset game state
        user_mode = False
        comp_mode = False
        
        # exit main game loop
        game_on = False
        
#---HELP HANDLING---#
# prints help text to the console
## Created by: Michelle
def user_help():
    print(txt.help_text)

#---HINT HANDLING---#
# gives the user the next character in the code
## Created by: Max
def user_hint():
    
    # bring global hint count into the functional namespace
    global hint_count
    
    # initialize hint string
    hint = secret_code[0:hint_count+1]
    
    # fill in the rest of the hint with '-'   
    while len(hint) < 4:
       hint += return_pegs[2]
       
    # print hint to console
    print("\nHINT:", hint)
    
    # increment number of hints used
    hint_count += 1
  
#---GUESS EVALUATION---#
## Created by: Sam
# checks if the user guessed the right sequence of colors
def evaluate_guess(temp_guess, temp_code):

    # create return pegs string for user guess feedback
    return_code = ""
    
    # if the guess has the right color and place add an 'X' to the return code
    for i in range(len(temp_guess)):
        if temp_guess[i] == temp_code[i]:
            return_code += return_pegs[0]
            temp_code[i] = "_"
            temp_guess[i] = "_"
    
    # if the guess has the right color but wrong place add an 'O' to the return code
    # added new conditional and to make sure that the same character in the string wasn't being read
    # after replace
    temp_code = "".join(temp_code)
    for i in range(len(temp_guess)):
        if temp_guess[i] != temp_code[i] and temp_guess[i] in temp_code and temp_guess[i] != "_":
            return_code += return_pegs[1]
            # remove the letter being evaluated in the guess from the temporary secret code
            temp_code = temp_code.replace(temp_guess[i], "_", 1)
            
    # fill in the rest of the return code with '-' for incorrect colors        
    while len(return_code) < 4:
        return_code += return_pegs[2]
        
    # reformat return code
    return_code = "".join(sorted(return_code))[::-1]
    
    # return return pegs to give feedback to user via console 
    return return_code

#---WIN HANDLING---#
## Created by: Sam
def user_win():
    # display win message
    print ("\nCONGRATULATIONS YOU CRACKED THE CODE!!")
    # display stats
    print ("Number of Tries:", tries)
    print ("Number of Hints:", hint_count)
    #calculate and print score
    score = calc_score()
    print ("Final Score:", score) 
    
    # go to continue screen
    continue_screen()

## Created by: Max
def comp_win():
    # display win message
    print ("\nTHE CODE IS CRACKED!!")
    # display stats
    print ("Number of Tries:", tries)
    #calculate and print score
    score = calc_score()
    print ("Final Score:", score) 
    
    # go to continue screen
    continue_screen()


#--LOSE HANDLING---#
## Created by: Sam
def lose():
    # display lose message
    print ("\nYOU HAVE FAILED TO CRACK THE CODE!!")
    # bring global game state into the functional namespace
    global game_on
    global user_mode
    global comp_mode
    
    # reset game state
    user_mode = False
    comp_mode = False
    
    # exit main game loop
    game_on = False
    # go to continue screen
    continue_screen()    
    
#---CALCULATE SCORE---#
## Created by: Sam
def calc_score():
    score = 5000 - ((200 * tries) + (1000 * hint_count))
    return score

#---CONTINUE HANDLING---#
## Created by: Max
def continue_screen():
    
    global game_on
    global user_mode
    global comp_mode
    
    game_on = False
    user_mode = False
    comp_mode = False

#---INITIALIZE COMP MODE---#
## Created by: Max
def init_comp_mode():
    
    global secret_code
    global comp_mode
    
    # print user mode instructions
    print(txt.comp_mode_instr)
    
    # prompt user to input secret code
    secret_code = comp_secret_prompt()
    
    # turn on user mode loop
    comp_mode = True

#---SECRET CODE INPUT---#
## Created by: Max
def comp_secret_prompt():
    
    global secret_code
    
    # prompt user to enter their secret code
    secret_code = input("Enter the secret code: ").upper()
    
    secret_code = comp_secret_format(secret_code)
    
    return secret_code

#---FORMAT CODE INPUT---#
## Created by: Michelle
def comp_secret_format(secret_code):
    
    # set to false if user uses incorrect format
    correct_format = True
    
    # sanitize input, remove any seperator chars and rejoin
    secret_code = re.split("[., \-!?$@#*+-;<>:%^&]+", secret_code)
    secret_code = "".join(secret_code)    
      
    # check if user typed QUIT
    if secret_code == "QUIT":
        quit_game()
        
    # make sure the user's guess is the correct length
    elif len(secret_code) != 4:
        print("Please enter 4 colors.")
        correct_format = False

    # check if user used correct colors in their code
    elif any(c not in color_pegs for c in secret_code): 
        print ("Please only use the following colors:", color_pegs)
        correct_format = False  
        
    # if user doesn't use the correct format reprompt them
    if correct_format == False:
       secret_code = comp_secret_prompt()
       
    return secret_code


#---KNUTH'S ALGORITHM---#
## Created by: Max
"""
 1. Create a set S of remaining possibilities (at this point there are 1296). 
    The first guess is aabb.

 2. Remove all possibilities from S that would not give the same score of 
    colored and white pegs if they were the answer.

 3. For each possible guess (NOT necessarily in S) calculate how many possibilities 
    from S would be eliminated for each possible colored/white score. 
    The score of the guess is the least of such values. 
    Play the guess with the highest score (minimax).

 4. Go back to step 2 until you have got it right.
"""

def knuths():

    global tries
    
    # create a set of all possible secret codes
    all_codes = [''.join(code) for code in product(''.join(color_pegs), repeat=4)]
    possible_codes = [''.join(code) for code in product(''.join(color_pegs), repeat=4)]
    
    # all possible resulting strings of code evaluation
    possible_returns = ["XXXX","XXX-","XXOO","XXO-","XX--","XOOO","XOO-","XO--","X---","OOOO","OOO-","OO--","O---","----"]
    
    print("\nSolving...")
    
    # crack the code in at most 5 tries
    crack(set(possible_codes), set(possible_returns), set(all_codes))
        
# break the secret code in at most 5 tries
def crack(possible_codes, possible_returns, all_codes):
    
    global tries
    
    # print remaining possible codes after the first try
    if tries != 0:
        print("\nRemaining possible codes:", possible_codes)
    
    # display try count
    print("\nTry:", tries+1)
    
    # if this is the first try guess "AABB"
    if tries == 0:
        comp_guess = "PPOO"
        
    # if there is one choice left in the list of possible codes guess it 
    elif len(possible_codes) == 1:
        	comp_guess = possible_codes.pop()
    
    # make a guess that best satisifies minimax
    else:                
        # choose the next guess with knuth's minimax function
        comp_guess = max(all_codes, key=lambda x: min(sum(1 for code in possible_codes if evaluate_guess(list(code), list(x)) != result) for result in possible_returns))
        
    # display computer guess
    print("\nComputer guess:", comp_guess)
    
    # hold the return pegs of guess in guess_score  
    guess_score = evaluate_guess(list(comp_guess), list(secret_code))
    
    # output return pegs to console
    print("\nReturn pegs:", guess_score)
    
    # increment number of tries
    tries += 1
    
    # if the computer gets the code end the game
    if guess_score == "XXXX": 
        comp_win()
        
    else:      
        # remove all possibilities from S that would not give the same score of colored and white pegs if they were the answer.
        possible_codes -= set(code for code in possible_codes if evaluate_guess(list(comp_guess), list(code)) != guess_score)
        
        # crack again with remaining set of possible secrets
        crack(possible_codes, possible_returns, all_codes)

##################
#   START GAME   #
##################
        
## Created by: Max
        
# ensures that both game_on loops can be reached at any point
while True:
    
    # loops while the game is set to on    
    while game_on:
        
        # print the title of the game
        print (txt.title)
        
        # prompt user to select their game mode
        select_game_mode()

        
        #################
        #   USER MODE   #
        #################
        
        # the computer generates a secret code and the user tries to guess
        
        while user_mode:
            
#            ## TEST SECRET CODE
#            print ("\nsecret code =", secret_code)
            
            # check if user expended all their tries
            if tries >= difficulties[game_difficulty]:
                lose()
                
                
            # prompt user for guess and check formatting
            if tries < difficulties[game_difficulty]:
                user_guess= user_guess_prompt()
            
            # if user input is not one of the reserved commands evaluate guess
            if user_guess not in special_commands and tries < difficulties[game_difficulty]:
                
                # increment number of tries
                tries += 1
                
                # print user guess to console
                print ("Your guess:", user_guess)
                
                # evaluate user guess and print return pegs
                return_code = evaluate_guess(list(user_guess), list(secret_code))
                
                # if the user enters the correct code, display stats and exit
                if return_code == "XXXX":
                    user_win()
                
                # if the user enters a wrong code display the return pegs to the console
                else:
                    print("\nReturn code:", return_code)  
            
            
            
        #################
        #   COMP MODE   #
        #################
                
        # the user generates a secret code and the computer tries to guess
        
        while comp_mode:
            
            # display entered code
            print("Your secret code =", secret_code)
            
            if secret_code not in special_commands:
                # run knuth's algorithm until the code is solved
                knuths()
            
           # go to continue screen if user enters special command 'quit'        
            continue_screen()
        
    #################
    #   CONTINUE?   #
    #################
   
    # loops while the game is set to off	
    while not game_on:
                
        # reset stats
        tries = 0
        hint_count = 0
        
        # reset game state
        user_mode = False
        comp_mode = False
        game_difficulty = ''
        
        # ask the user if they would like to play again
        play_again = input("\nDo you want to play again [y/n]: ").upper()	

        # if no exit
        if play_again == "N":
            sys.exit("Thanks for playing!")
        # if yes restart the game
        elif play_again == "Y":
            game_on = True
            print(game_on)
        else:
            print("Please enter 'y' for yes and 'n' for no!")
