import random
import alt_door

def live():

    # preset variables
    total_win = 0
    total_plays = 0
    win_plays_list = []
    switch_counter = 0
    switch_win = 0
    repeat = "y"



    # randomizer
    while repeat[0] == "y":
        print("Welecome to random door: ")
        prize = random.randint(1, 3)
        # print("psst... the prize is behind door #", prize)
        print(" 1) ????\n 2) ????\n 3) ????")

        # user picks a door 
        valid_door = False
        while valid_door == False:
            user_door = input("Pick a door between 1 and 3: ")
            if '0' < user_door < '4':
                valid_door = True
                user_door = int(user_door)
            else:
                print("No such door exits please try again: ")

        # user is shown another option and ask if they want to switch
        altdoor = alt_door.alt_door(prize, user_door)
        switch = str.lower(input(
            f"Door {altdoor} is dish detergent. Would you like to change doors? y/n "))
        if switch[0] == "y":
            user_door = alt_door.switch(altdoor, user_door)
            switch_counter += 1

        # door is revealed 
        if user_door == prize:
            print("Congraduations, you won $10,000!!!")
            total_win += 1
        else:
            print("You got dish detergent.")
        
        if switch[0] == "y" and user_door == prize:
            switch_win += 1    
        
        total_plays += 1
        repeat = str.lower(input("would you like to countinue? Enter y/n: "))
    
    original_choice = (total_plays - switch_counter)
    original_choice_win = (total_win - switch_win)
    win_plays_list.append(total_win)
    win_plays_list.append(total_plays)
    win_plays_list.append(switch_counter)
    win_plays_list.append(switch_win)
    win_plays_list.append(original_choice)
    win_plays_list.append(original_choice_win)

    return win_plays_list

    