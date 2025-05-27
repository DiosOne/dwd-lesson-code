# dog.py

'''
--- MODIFY TASKS ---

1. Add a new instance variable age to our Dog.

2. Add a new method 'celebrate_birthday' that increases the dog's age by 1 and prints a message.
'''

class Dog:
    # This is the constructor method
    def __init__(self, name, breed, age):
        print(f"A new dog named {name} is being created!")
        self.name = name  # Instance variable
        self.breed = breed # Instance variable
        self.age = age

    # This is a method
    def bark(self):
        print(f"{self.name} says: Woof!")
        
    def celebrate_bday(self):
        self.age += 1
        print(f'Happy birthday {self.name}, you are now {self.age} years old')

    def describe(self):
        print(f"{self.name} is a {self.breed}.")

# --- Let's USE the Dog class ---
print("--- Creating and Using Dog Objects ---")
# Create an object (instance) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 3)

# Create another object
dog2 = Dog("Lucy", "Poodle", 6)

# Call methods on the objects
dog1.describe()
dog1.bark()
dog1.celebrate_bday()

print("-" * 10) # Separator

dog2.describe()
dog2.bark()
dog2.celebrate_bday()

print("\n--- Accessing Instance Variables (generally done via methods) ---")
print(f"Dog 1's name is: {dog1.name}")
print(f"Dog 2's breed is: {dog2.breed}")
