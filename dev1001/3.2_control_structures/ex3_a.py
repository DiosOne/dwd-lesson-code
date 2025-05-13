'''basic ternary operator funcction'''
# Ternary: You have a variable is_member (Boolean).

IS_MEMBER= True
# normal_rate= 100

# if is_member== True:
#     discount_rate== * 0.1

DISCOUNT_RATE=  0.10 if IS_MEMBER else 0.02


# If is_member is True, discount_rate is 0.10, else it's 0.02.
# Use the ternary operator. Print the discount_rate.


print(DISCOUNT_RATE)

# is_member: True
# discount_rate = 0.10 if True else 0.02
# print(f'Discount Rate: {discount_rate:.2f}%')
