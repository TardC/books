from user import User

class Privileges():
    """Simulate administrators' privileges."""

    def __init__(self, privileges=['can add post',
                                   'can delete post',
                                   'can ban user']):
        """Initialize the attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Show administrators' privileges."""
        print("Administrators have the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    """Simulate an administrator, a user who has privileges."""

    def __init__(self, first_name, last_name, sex, age):
        """
        Initialize the attributes of the parent class, then initialize
        the unique attributes of administrators.
        """
        super().__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()
