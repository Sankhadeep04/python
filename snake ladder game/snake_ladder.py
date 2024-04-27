import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, steps):
    player += steps
    # old_pos = player
    # print("old pos ",old_pos)
    if player > 100:
        player -= steps
    # print(player,"player")
    return player

def check_snake_or_ladder(player):
    ladders = {2:38 , 4:14, 9:31, 21:42 , 28:84 , 51:67 , 72:91 , 80:99}
    snakes = {17:7 , 54:34 , 62:19 , 64:60 , 87:36 , 93:73 , 94:75 ,98:79}
    if player in ladders:
        new_position = ladders[player]
        if new_position > player:
            print("You climbed a ladder! You are now at position", new_position)
            return new_position
    elif player in snakes:
        new_position = snakes[player]
        if new_position < player:
            print("Oops! You encountered a snake. You are now at position", new_position)
            return new_position
    return player


def play_snake_and_ladder():
    position = 0
    while True:
        input("Press Enter to roll the dice: ")
        dice = roll_dice()
        print("You rolled a", dice)
        if position == 0 and dice !=1:
            print("You need a 1 to start")
        else:    
            position = move_player(position, dice)
            position = check_snake_or_ladder(position)
            print("You are now at position", position)
            if position == 100:
                print("Congratulations! You reached at 100 and won!")
                break
play_snake_and_ladder()