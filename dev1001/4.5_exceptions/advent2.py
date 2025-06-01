try:
    attack_power= int(input('Enter you attack: '))
    enemy_def= int(input('Enter enemy defence (non-zero): '))
    damage= attack_power/enemy_def* 10
    print(f'you dealt {damage} damage')
except ValueError as err:
    print(f'An error occured: {err}')
except ZeroDivisionError as err:
    print(f'An error occured: {err}')