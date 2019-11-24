class User():
    """Simulate a user."""

    def __init__(self, first_name, last_name, sex, age):
        """Initialize the attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Print the user's information summary."""
        full_name = self.first_name + " " + self.last_name
        print("The user's name is " + full_name.title() +
              ", sex is " + self.sex +
              ", and age is " + str(self.age) + ".")

    def greet_user(self):
        """Send personalized greetings to the user."""
        full_name = self.first_name + " " + self.last_name
        print("Hello, " + full_name.title() + "!")

    def increment_login_attempts(self):
        """Add 1 to the login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0
