import unittest
import math

MAX_VOLUME_CM3 = 1000000
MAX_DIMENSION_CM = 150
MAX_MASS_KG = 20

class TestSmarterTech(unittest.TestCase):
    def run_test(self):
        long_dimension = math.cbrt(MAX_VOLUME_CM3)
        medium_dimension = long_dimension/2
        short_dimension = long_dimension/4
        self.assertEqual(sort(medium_dimension, long_dimension, long_dimension, MAX_MASS_KG/2), 'STANDARD')
        self.assertEqual(sort(long_dimension, long_dimension, long_dimension, MAX_MASS_KG/2), 'SPECIAL')
        self.assertEqual(sort(long_dimension*2, long_dimension, long_dimension, MAX_MASS_KG), 'REJECTED')
        self.assertEqual(sort(MAX_DIMENSION_CM*2, medium_dimension, medium_dimension, 1), 'SPECIAL')
        self.assertEqual(sort(MAX_DIMENSION_CM, short_dimension, short_dimension, MAX_MASS_KG), 'REJECTED')
        self.assertEqual(sort(short_dimension, short_dimension, short_dimension, MAX_MASS_KG), 'SPECIAL')
        with self.assertRaises(ValueError):
            sort(-1, short_dimension, short_dimension, MAX_MASS_KG)
        with self.assertRaises(ValueError):
            sort(short_dimension, -1, short_dimension, MAX_MASS_KG)
        with self.assertRaises(ValueError):
            sort(short_dimension, short_dimension, -1, MAX_MASS_KG)
        with self.assertRaises(ValueError):
            sort(short_dimension, short_dimension, short_dimension, -MAX_MASS_KG)
        with self.assertRaises(ValueError):
            sort(long_dimension*20, long_dimension, long_dimension, MAX_MASS_KG/2)

def sort(width, height, length, mass):
    if any([n < 0 for n in [width, height, length, mass]]):
        raise ValueError
    volume = length*height*width
    bulky = volume > MAX_VOLUME_CM3 or any([dimension > MAX_DIMENSION_CM for dimension in
                                            [width, height, length]])
    if bulky and mass > MAX_MASS_KG:
        return 'REJECTED'
    if bulky or mass > MAX_MASS_KG:
        return 'SPECIAL'
    return 'STANDARD'
