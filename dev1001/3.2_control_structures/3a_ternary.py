'''_summary_'''
# --- USE: Ternary Operator ---
AGE = 22
CATEGORY= "adult" if AGE >= 18 else "Minor" # The ternary operator
# if AGE >= 18:
#     CATEGORY= 'Adult'
# else:
#     CATEGORY= 'Minor'


print(f"Age: {AGE}, Category: {CATEGORY}")

# read more on ternary
# what makes a ternary?

# so instead of putting a simple value for the variable,
    # the use purpose of the 'ternary expression' is
    # like interpolating an 'expression (similar to a formula using if/else statement)
    # to determine between the value options (adult/minor) to be assigned to the variable (category)

# Ternary (3a): Rewrite the ternary assignment for category using a
#   traditional if-else block to demonstrate equivalence.
#   Then, change the condition in the ternary operator:
#   if age < 13, category is "Child", else it's "Teen or Adult".
