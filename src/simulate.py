import random
import alt_door


def simulate(gamemode):

    # preset variables
    total_win = 0
    total_plays = 0
    win_plays_list = []
    switch_counter = 0
    switch_win = 0
    
    # 1 of 2 times user imput is needed
    valid_sim = False
    while valid_sim == False:
        repeat = input("Enter the number of time you want to simulate: ")
        try:
            int(repeat)
            valid_sim = True
        except:
            ValueError
            print("please try again")
    repeat = int(repeat)

    for i in range(repeat):
        print("Welecome to random door: ")
        prize = random.randint(1, 3)
        print(" 1) ????\n 2) ????\n 3) ????")

        # reset randomizer
        random.seed()
        user_door = random.randint(1, 3)
        print(f"Pick a door between 1 and 3: {user_door} ")
        switch = random.randint(1, 2)
        if switch == 1:
            switch = "y"
            switch_counter += 1
        else:
            switch = "n"
        altdoor = alt_door.alt_door(prize, user_door)   
        print(
            f"Door {altdoor} is dish detergent. Would you like to change doors? y/n {switch}")
        if switch[0] == "y":
            user_door = alt_door.switch(altdoor, user_door)

        # door is revealed
        if user_door == prize:
            print("Congraduations, you won $10,000!!!")
            total_win += 1
        else:
            print("You got dish detergent.")
        
        if switch == "y" and user_door == prize:
            switch_win += 1
            
        total_plays = i + 1
    
    original_choice = (total_plays - switch_counter)
    original_choice_win = (total_win - switch_win)
    win_plays_list.append(total_win)
    win_plays_list.append(total_plays)
    win_plays_list.append(switch_counter)
    win_plays_list.append(switch_win)
    win_plays_list.append(original_choice)
    win_plays_list.append(original_choice_win)
    return win_plays_list
