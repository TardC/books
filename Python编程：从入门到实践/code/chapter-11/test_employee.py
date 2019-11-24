import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Test Employee.py"""

    def setUp(self):
        """Create a Employee object."""
        self.my_employee = Employee('tard', 'c', 150000)

    def test_give_default_raise(self):
        """Test the default arguement will work well."""
        self.my_employee.give_raise()
        self.assertEqual(155000, self.my_employee.year_salary)

    def test_give_custom_raise(self):
        """Test a custom arguement will work well."""
        self.my_employee.give_raise(20000)
        self.assertEqual(170000, self.my_employee.year_salary)

unittest.main()
