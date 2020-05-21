import random
import time
from db_setup import read_data_from_db


answer = input("""Welcome, would you like to play charades?\n
Type 'y' for yes or anything else to quit.
\n >>>> """
)

if str.lower(answer) == 'y':
    print("Great, let's get started!")

    selection = input("""Pick a movie by typing in the number
1. Frozen
2. Toy Story
\n >>>> """
)

    # load the characters
    char_list = read_data_from_db(int(selection))

    rounds = input(str(len(char_list)) +
                   """ characters retrieved.\nHow many rounds do you want to play?\n>>>> """)

    for curr_round in range(1, int(rounds) + 1):
        playing = input(""" Ready? 'y' for yes, any key to quit\n>>>> """)
        if playing == 'y':
            print(char_list[random.randint(0, len(char_list) - 1)])
            time.sleep(1)
            print("Times up!")
        else:
            print("Thanks for playing! See you later")
            exit()

    # completed all rounds
    print("Thanks for playing! See you later")

else:
    print("See you later")
