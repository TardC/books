class Employee():
    """Simulate an employee."""

    def __init__(self, first_name, last_name, year_salary):
        """Initiate attributes first name, last name and year salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.year_salary = year_salary

    def give_raise(self, salary_raise=5000):
        """Give the year salary a raise."""
        self.year_salary += salary_raise
