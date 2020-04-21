import unittest
import calc

# From tutorial: https://www.youtube.com/watch?v=6tNS--WetLI

class TestCalc(unittest.TestCase):
# For list of inherited methods see: https://docs.python.org/3/library/unittest.html#test-cases

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)

        # Use the context manager to test exception values
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
   unittest.main()
