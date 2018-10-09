# title of the game
title = """
==========================================================================
  __  __           _____ _______ ______ _____  __  __ _____ _   _ _____  
 |  \/  |   /\    / ____|__   __|  ____|  __ \|  \/  |_   _| \ | |  __ \ 
 | \  / |  /  \  | (___    | |  | |__  | |__) | \  / | | | |  \| | |  | |
 | |\/| | / /\ \  \___ \   | |  |  __| |  _  /| |\/| | | | | . ` | |  | |
 | |  | |/ ____ \ ____) |  | |  | |____| | \ \| |  | |_| |_| |\  | |__| |
 |_|  |_/_/    \_\_____/   |_|  |______|_|  \_\_|  |_|_____|_| \_|_____/ 

==========================================================================
"""

# instructions for the user to select their game mode
game_mode_instr = """
+-----------------------------------------------------------------------+
|                             How to Play:                              |
|                                                                       |
| Welcome to MASTERMIND!!!                                              |
| The world famous code cracking game!                                  |
|                                                                       |
| Please begin by entering your desired game mode in the console below: |
| - [U]ser Mode: The computer generates a code and you try to crack it! |
| - [C]omp Mode: You enter a code for the computer to try to crack!     |
+-----------------------------------------------------------------------+
"""

user_mode_instr = """
    +---------------------------------------------------------------+
    |                          USER MODE:                           |
    |                                                               |
    | Try to guess the secret code in as few tries as possible!     |
    |                                                               |
    | The code is a 4 length combination of the following 6 colors: |
    |                                                               |
    | [R]ed, [G]reen, [B]lue, [Y]ellow, [O]range, and [P]urple      |
    |                                                               |
    | Input your guess as a 4 letter string                         |
    | (e.g. RGBY or rgby)                                           |
    |                                                               |
    | DIFFICULTY SETTINGS:                                          |
    | - [E]asy: 25 tries to guess the code                          |
    | - [M]edium: 15 tries to guess the code                        |
    | - [H]ard: 5 tries to guess the code                           |
    |                                                               |
    | RETURN CODE:                                                  |
    | - 'X': right color in the right place                         |
    | - 'O': right color in the wrong place                         |
    | - '-': wrong color in the wrong place                         |
    |(WARNING: Return code positions don't correspond to your guess)|
    |                                                               |
    | SPECIAL COMMANDS:                                             |
    | - HELP: get a quick refresher on how to play                  |
    | - HINT: get the next color in the secret code                 |
    | - QUIT: quit out of the game                                  |
    +---------------------------------------------------------------+
"""

help_text="""  
     ???????????????????????????????????????????????????????????????
     +-------------------------------------------------------------+
     | It seems that you have asked for help!                      |
     |                                                             |
     | Please enter a 4 letter color string to guess the           |
     | computer's secret code.                                     |
     |                                                             |                 
     | After a guess, you will be returned two types of pegs:      |
     |    - X's to signify there is a peg with the right color     |
     |       in the right position                                 |
     |     - O's to signify there is a peg with the right color    |
     |       in the wrong position.                                |
     |                                                             |
     | The order of the pegs does not correlate to the positions   |
     | in your guess.                                              |        
     |                                                             |
     | You can also ask for a hint at any time by typing 'hint' or |
     | quit/end the game at any time by typing 'quit'.             |
     |                                                             |
     | You will be allowed 25, 15, or 5 tries to guess the code,   |
     | depending on the difficuty you have selected.               |
     |                                                             |
     | Good Luck!                                                  |
     +-------------------------------------------------------------+
     ???????????????????????????????????????????????????????????????
"""

comp_mode_instr = """
    +----------------------------------------------------------------+
    |                           COMP MODE:                           |
    |                                                                |
    |  Enter a secret code and watch as the computer                 |
    |  magically gets it in as few tries as possible!                |
    |                                                                |
    |  The code is a 4 length combination of the following 6 colors: |
    |                                                                |
    |  [R]ed, [G]reen, [B]lue, [Y]ellow, [O]range, and [P]urple      |
    |                                                                |
    |  Input your code as a 4 letter string                          |
    |  (e.g. RGBY or rgby)                                           |
    |                                                                |
    |  SPECIAL COMMANDS:                                             |
    |  - QUIT: quit out of the game                                  |
    +----------------------------------------------------------------+
"""
