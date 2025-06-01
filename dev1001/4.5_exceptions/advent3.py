


def enter_dungeon(level):
    if level < 5:
        raise ValueError('You shall not pass!')
    else:
        print('You enter dungeon')
        
        
# Main
try:
    player_level= int(input('Enter player level: '))
    enter_dungeon(player_level)
except ValueError as err:
    print(f'Access denied: {err}')