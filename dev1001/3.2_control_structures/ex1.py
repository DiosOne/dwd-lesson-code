# Has a variable item_price.
# Has a variable customer_has_coupon (set to True or False).
# If customer_has_coupon is True, apply a 10% discount to item_price to get final_price.
# Else, final_price is the same as item_price.
# Print the final_price.
# Test with customer_has_coupon being both True and False."

item_price= 100
customer_has_coupon= True
if customer_has_coupon == True:
    final_price= item_price * 0.9
else: 
    final_price= item_price
print (final_price)
