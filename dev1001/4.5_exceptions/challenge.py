'''Develop a function that lets a player choose a weapon.
It should check that the chosen weapon is in the available list.
It should raise a ValueError if not.
It should also raise a custom LockedItemError (you must define this exception) if the chosen weapon is locked.'''

available_weapons = ["sword", "bow", "staff"]
locked_weapons = ["legendary sword"]


def choose_weapon():
    # weapon= input('choose weapon: ')
    for weapon in available_weapons:
        if weapon== available_weapons:
            print(f'You have chosen {weapon}')
    else:
        print('Weapon na')
        
choose_weapon()
    




# '''
# Task:
# Fix the GameEngine.run_turn() method. It loads data from a file, interprets a command, and checks health. Use:

# - try...except
# - specific error types
# - custom exception
# - raise
# '''
# class GameError(Exception):
#     pass

# class GameEngine:
#     def __init__(self, player_health):
#         self.health = player_health

#     def run_turn(self, command, data_file):
#         try:
#             #It loads data from a file
#             with open(data_file) as f:
#                 data= f.read()
#                 #interprets a command
#                 if command== 'jump':
                
#         except:
            
#         # You complete this
#         # pass

# engine = GameEngine(5)
# engine.run_turn("jump", "bad_file.txt")