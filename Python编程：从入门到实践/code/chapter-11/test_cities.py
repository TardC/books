import unittest
from city_functions import get_formatted_cityname

class CitynamesTestCase(unittest.TestCase):
    """Test city_functions.py"""

    def test_city_country(self):
        """Can it correctly handle a cityname like Santiago, Chile?"""
        formatted_cityname = get_formatted_cityname('santiago', 'chile')
        self.assertEqual(formatted_cityname, 'Santiago, Chile')

    def test_city_country_population(self):
        """
        Can it correctly handle a cityname like
        Santiago, Chile - population 5000000?
        """
        formatted_cityname = get_formatted_cityname(
            'santiago', 'chile', population=5000000)
        self.assertEqual(
            formatted_cityname, 'Santiago, Chile - population 5000000')

unittest.main()
