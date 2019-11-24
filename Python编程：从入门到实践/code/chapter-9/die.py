from random import randint

class Die():
    """Simulate a die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Simulate rolling the die."""
        random_integer = randint(1, self.sides)
        print("The random integer is: " + str(random_integer))

die = Die()
i = 0
while i < 10:
    die.roll_die()
    i += 1

die = Die(10)
i = 0
while i < 10:
    die.roll_die()
    i += 1

die = Die(20)
i = 0
while i < 10:
    die.roll_die()
    i += 1
