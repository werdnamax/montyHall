import random

def alt_door(prize, user_door):
    door = [1, 2, 3]
    door.remove(prize)
    if user_door != prize:
        door.remove(user_door)
        return door[0]
    else:
        return random.choice(door)


def switch(altdoor, user_door):
    for j in range(1, 4):
        if (j != user_door and j != altdoor):
            return j