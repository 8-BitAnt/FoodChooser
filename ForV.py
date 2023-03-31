# Favorite Food Picker

# Fruits Dictionary
fruits = {
    'sweet': {
        'red': ['Red Apple'],
        'orange': ['Orange'],
        'yellow': ['Banana'],
        'green': ['Pear']
    },
    'sour': {
        'red': ['Tart Cherries'],
        'orange': ['Gooseberries'],
        'yellow': ['Lemons'],
        'green': ['Lime']
    }
}

# Vegetables Dictionary
vegetables = {
    'sweet': {
        'red': ['Tomato'],
        'orange': ['Sweet Potatoe'],
        'yellow': ['Corn'],
        'green': ['Peas']
    },
    'spicy': {
        'red': ['Bell Pepper'],
        'orange': ['Habanero Pepper'],
        'yellow': ['Banana Pepper'],
        'green': ['Jalapeno Pepper']
    }
}

# Asks the user if they want to start with fruits or vegetables.
ForV = input("Weclome to the favortie food picker! \nWould you like to start with your favorite fruit or vegetable?: ").lower()

while ForV not in ["fruit","vegetable"]:
  print("Invalid input, please type fruit or vegetable.")
  ForV = input("Would you like to start with your favorite fruit or vegetable?: ").lower()

# Asks the user if they want to continue with the taste or color.
TorC = input("Would you like to continue with the taste or the color?: ").lower()

while TorC not in ["taste","color"]:
  print("Invalid input, please type taste or color.")
  TorC = input("Would you like to continue with the taste or the color?: ").lower()


# This is if the user starts with taste after choosing fruit.
if ForV == "fruit":
  if TorC == "taste":
    
    SorS = input("Would you prefer a sweet or sour fruit?: ").lower()

    while SorS not in ["sweet","sour"]:
      print("Invalid input, please type sweet or sour.")
      SorS = input("Would you prefer a sweet or sour fruit?: ").lower()

    ROYG = input("Choose red, orange, yellow or green: ").lower()

    while ROYG not in ["red","orange","yellow","green"]:
      print("Invalid input, please type red, orange, yellow or green.")
      ROYG = input("Choose red, orange, yellow or green: ").lower()
    
	# End of program.
    print(f"Your favorite fruit is: {fruits[SorS][ROYG][0]}")

# This is if the user starts with color after choosing fruit.
if ForV == "fruit":
  if TorC == "color":

    ROYG = input("Choose red, orange, yellow or green: ").lower()

    while ROYG not in ["red","orange","yellow","green"]:
      print("Invalid input, please type red, orange, yellow or green.")
      ROYG = input("Choose red, orange, yellow or green: ").lower()
    
    SorS = input("Would you prefer a sweet or sour fruit?: ").lower()

    while SorS not in ["sweet","sour"]:
      print("Invalid input, please type sweet or sour.")
      SorS = input("Would you prefer a sweet or sour fruit?: ").lower()
    
	# End of program.
    print(f"Your favorite fruit is: {fruits[SorS][ROYG][0]}")

# This is if the user starts with taste after choosing vegetable.
if ForV == "vegetable":
  if TorC == "taste":
    
    SorS = input("Would you prefer a sweet or spicy vegetable?: ").lower()

    while SorS not in ["sweet","spciy"]:
      print("Invalid input, please type sweet or sour.")
      SorS = input("Would you prefer a sweet or spicy vegetable?: ").lower()

    ROYG = input("Choose red, orange, yellow or green: ").lower()

    while ROYG not in ["red","orange","yellow","green"]:
      print("Invalid input, please type red, orange, yellow or green.")
      ROYG = input("Choose red, orange, yellow or green: ").lower()
    
	# End of program.
    print(f"Your favorite vegetable is: {vegetables[SorS][ROYG][0]}")

# This is if the user starts with color after choosing vegetable.
if ForV == "vegetable":
  if TorC == "color":

    ROYG = input("Choose red, orange, yellow or green: ").lower()

    while ROYG not in ["red","orange","yellow","green"]:
      print("Invalid input, please type red, orange, yellow or green.")
      ROYG = input("Choose red, orange, yellow or green: ").lower()
    
    SorS = input("Would you prefer a sweet or spicy vegetable?: ").lower()

    while SorS not in ["sweet","spicy"]:
      print("Invalid input, please type sweet or sour.")
      SorS = input("Would you prefer a sweet or spicy vegetable?: ").lower()
    
	# End of program.
    print(f"Your favorite vegetable is: {vegetables[SorS][ROYG][0]}")