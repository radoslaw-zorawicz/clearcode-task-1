import unittest
import hack_power


class TestHackModule(unittest.TestCase):

    def test_compute_power_of_valid_hacks(self):
        valid_hacks = {
            'baaca': 31,
            'babacaba': 55,
            'aabacabaaaca': 81,
            'abc': 6
        }
        for hack, power in valid_hacks.items():
            self.assertEqual(power, hack_power.hack_calculator(hack))

    def test_return_zero_power_for_invalid_hacks(self):
        invalid_hacks= ['baad', 'ba a', 'baaba*b$', 'cbac12b']
        for hack in invalid_hacks:
            self.assertEqual(0, hack_power.hack_calculator(hack))

    def test_return_zero_power_for_empty_hack(self):
        self.assertEqual(0, hack_power.hack_calculator(""))

if __name__ == '__main__':
    unittest.main()