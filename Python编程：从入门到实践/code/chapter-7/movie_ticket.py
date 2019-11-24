# ~ while True:
    # ~ age = input("What is your age? ")
    # ~ age = int(age)

    # ~ if age < 3:
        # ~ price = 0
    # ~ elif age < 12:
        # ~ price = 10
    # ~ elif age >= 12:
        # ~ price = 15

    # ~ print("Your ticket price is " + str(price) + ".")


# 7-6
age = 0
while age != 'quit':
    age = input("What is your age? ")
    if age != 'quit':
        age = int(age)

        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        elif age >= 12:
            price = 15

        print("Your ticket price is " + str(price) + ".")


age = input("What is your age? ")
while age != 'quit':
    age = int(age)

    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    elif age >= 12:
        price = 15

    print("Your ticket price is " + str(price) + ".")

    age = input("What is your age? ")

# ~ active = True
# ~ while active:
    # ~ age = input("What is your age? ")

    # ~ if age == 'quit':
        # ~ active = False
    # ~ else:
        # ~ age = int(age)

        # ~ if age < 3:
            # ~ price = 0
        # ~ elif age < 12:
            # ~ price = 10
        # ~ elif age >= 12:
            # ~ price = 15

        # ~ print("Your ticket price is " + str(price) + ".")


# ~ while True:
    # ~ age = input("What is your age? ")

    # ~ if age == 'quit':
        # ~ break
    # ~ else:
        # ~ age = int(age)

        # ~ if age < 3:
            # ~ price = 0
        # ~ elif age < 12:
            # ~ price = 10
        # ~ elif age >= 12:
            # ~ price = 15

        # ~ print("Your ticket price is " + str(price) + ".")
