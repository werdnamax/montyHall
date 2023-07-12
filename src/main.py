""" 
werdnaMax
Monty Hall Paradox "Gameshow" 
"""

import random
import simulate
import live

# seed and randomizer (last time user imput is needed)
seed = input("Enter a seed: ")
random.seed(seed)

# main 
while True:
    gamemode = str.lower(input("Live or simulation? enter L or S: "))
    if gamemode[0] == "l":
        win_plays_list = live.live()

        # unpacking the variables
        total_wins = win_plays_list[0]
        total_plays = win_plays_list[1]
        switch_counter = win_plays_list[2]
        switch_win = win_plays_list[3]
        original_choice = win_plays_list[4]
        original_choice_win = win_plays_list[5]
        
        # calcuating ratios
        total_win_lose = (total_wins / total_plays * 100)
        if switch_counter != 0:
            switch_win_loss = (switch_win / switch_counter * 100) 
        else:
            switch_win_loss = 0.0
        
        if original_choice != 0:
            original_choice_win_lose = (original_choice_win / original_choice * 100) 
        else:
            original_choice_win_lose = 0.0
        
        # gameplay results
        print()
        print(f'Out of {switch_counter} times you switched you won {switch_win} or %{switch_win_loss:.1f}')
        print(f'when staying with original door you won {original_choice_win} out of {original_choice} or %{original_choice_win_lose:.1f}')
        print(f"You won {total_wins} times out of {total_plays} total player %{total_win_lose:.1f} getting ${total_wins * 10000}. ")
        break 
    elif gamemode[0] == "s":
        win_plays_list = simulate.simulate(gamemode)

        # unpacking the variables
        total_wins = win_plays_list[0]
        total_plays = win_plays_list[1]
        switch_counter = win_plays_list[2]
        switch_win = win_plays_list[3]
        original_choice = win_plays_list[4]
        original_choice_win = win_plays_list[5]
        
        # calcuating ratios
        total_win_lose = (total_wins / total_plays * 100)
        if switch_counter != 0:
            switch_win_loss = (switch_win / switch_counter * 100) 
        else:
            switch_win_loss = 0.0
        
        if original_choice != 0:
            original_choice_win_lose = (original_choice_win / original_choice * 100) 
        else:
            original_choice_win_lose = 0.0

        # gameplay results
        print()
        print(f'Out of {switch_counter} times you switched you won {switch_win} or %{switch_win_loss:.1f}')
        print(f'when staying with original door you won {original_choice_win} out of {original_choice} or %{original_choice_win_lose:.1f}')
        profit: float = total_wins * 10000
        print(f"You won {total_wins} times out of {total_plays} total player %{total_win_lose:.1f} getting ${profit:,.2f}. ")
        break
    else:
        print("gamemode does not exits please try again")
