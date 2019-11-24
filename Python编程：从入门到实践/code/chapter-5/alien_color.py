# 1
alien_color = 'green'

if alien_color == 'green':
    print("You got 5 points.")


alien_color = 'red'

if alien_color == 'green':
    print("You got 5 points.")


# 2
alien_color = 'green'

if alien_color == 'green':
    print("You killed a green alien, got 5 points.")
else:
    print("You killed a other color alien, got 10 points.")


alien_color = 'red'

if alien_color == 'green':
    print("You killed a green alien, got 5 points.")
else:
    print("You killed a other color alien, got 10 points.")


# 3
alien_color = 'green'

if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15

print("You killed a " + alien_color + " alien, got " + str(score) + " points.")


alien_color = 'yellow'

if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15

print("You killed a " + alien_color + " alien, got " + str(score) + " points.")


alien_color = 'red'

if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15

print("You killed a " + alien_color + " alien, got " + str(score) + " points.")
