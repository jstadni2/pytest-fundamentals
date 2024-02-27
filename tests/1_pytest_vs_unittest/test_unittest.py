import unittest
from demos.math_operations import add_numbers, MathOperations


# EXAMPLE 1

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 10), 15)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)


# EXAMPLE 2

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()

    def test_add(self):
        self.assertEqual(self.math_ops.add(5, 10), 15)
        self.assertEqual(self.math_ops.add(-1, 1), 0)
        self.assertEqual(self.math_ops.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(self.math_ops.multiply(5, 10), 50)
        self.assertEqual(self.math_ops.multiply(-1, 1), -1)
        self.assertEqual(self.math_ops.multiply(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()