print('Welcome to Adventure')
gold=False
while not gold:
    gold_input= input('How much gold? ')
    try:
        gold= int(gold_input)
        x= gold/0
    except ValueError:
        print('Not a valid integer. Please enter whole numbers only')

print(f'You have {gold} gold coins')
print('Done')