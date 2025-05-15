def defeat_monsters():
    dungeon= [
        'Goblin',
        'Gold Coins',
        'Dragon',
        'Dragon',
        'Bandit',
        'Gold Coins',
        'Giant Snake'
    ]
    for i in range(len(dungeon)):
        dungeon[i]= 'Gold Coins'
        
    return dungeon

defeat_monsters()
