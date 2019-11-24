"""A group of classes used to represent electric vehicles."""

from car import Car

class Battery():
    """A simple attempt to simulate an electric car battery."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a message describing the battery capacity."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a message indicating the battery's cruising range."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery size."""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        The special features of electric vehicles.
        Initialize the properties of the parent class, then initialize
        the unique properties of electric vehicles.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
