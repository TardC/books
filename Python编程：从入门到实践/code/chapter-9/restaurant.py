class Restaurant():
    """Simulate a simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Summarize the restaurant's information."""
        print("The restaurant's name is " + self.restaurant_name +
              " and it's cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Point out that the restaurant is open."""
        print("The restaurant is open.")

    def set_number_served(self, number_served):
        """Set the number of people that have been served."""
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("The number of people who have been served" +
                  " cannot be reduced.")

    def increment_number_served(self, increment):
        """Increase the number of people served by increment."""
        if increment >= 0:
            self.number_served += increment
        else:
            print("The increment of people served cannot be negative.")


class IceCreamStand(Restaurant):
    """Simulate an ice cream stand, a special restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the attributes of the restaurant, then initialize
        the attributes of the ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Sweet Tube', 'Chocolate Cone', 'Apple Milkshake']

    def show_flavors(self):
        """Show the flavors of ice cream."""
        print("We have the following flavors of ice cream:")
        for flavor in self.flavors:
            print("- " + flavor)
