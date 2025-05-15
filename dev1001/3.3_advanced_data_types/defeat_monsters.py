'''module docstring'''
def defeat_monsters_in_dungeon():
    '''function docstring

    :return: _description_
    :rtype: _type_
    '''
    dungeon = [
        "Goblin", #0
        "Gold coins", #1
        "Dragon", #2
        "Dragon", #3
        "Bandit", #4
        "Gold coins", #5
        "Giant Snake"] #6
    dungeon[0]= 'Gold coins'
    dungeon[2]= 'Gold coins'
    dungeon[3]= 'Gold coins'
    dungeon[4]= 'Gold coins'
    dungeon[6]= 'Gold coins'
    # Defeat the monsters!
    return dungeon

defeat_monsters_in_dungeon()
