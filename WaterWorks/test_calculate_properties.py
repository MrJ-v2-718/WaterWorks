import random
import unittest
from math import pi
from water_works import calculate_properties


class TestCalculateProperties(unittest.TestCase):
    def test_calculate_properties(self):
        # Testing Criterion
        diameter_ft = random.randint(0, 600)
        diameter_in = random.randint(0, 12)
        height_ft = random.randint(0, 900)
        height_in = random.randint(0, 12)

        test_volume, test_surface_area, test_gallons_of_water, test_weight_of_water_pounds, test_head_pressure = (
            calculate_properties(diameter_ft, diameter_in, height_ft, height_in)
        )

        # Check if volume is calculated correctly
        radius_feet = (diameter_ft + diameter_in / 12) / 2
        height_feet = height_ft + height_in / 12
        volume = pi * (radius_feet ** 2) * height_feet
        self.assertEqual(test_volume, volume)

        # Check if surface area is calculated correctly
        surface_area = 2 * pi * (radius_feet ** 2) + 2 * pi * radius_feet * height_feet
        self.assertEqual(test_surface_area, surface_area)

        # Check if gallons of water are calculated correctly
        gallons_of_water = volume * 7.48052
        self.assertEqual(test_gallons_of_water, gallons_of_water)

        # Check if weight of water is calculated correctly
        weight_of_water_pounds = gallons_of_water * 8.330
        self.assertEqual(test_weight_of_water_pounds, weight_of_water_pounds)

        # Check if head pressure is calculated correctly
        head_pressure = height_feet / 2.31
        self.assertEqual(test_head_pressure, head_pressure)
