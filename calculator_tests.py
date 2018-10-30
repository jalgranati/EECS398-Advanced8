import calculator
import unittest
import random
class testAdd(unittest.TestCase):
    def test_random(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        self.assertEqual(x + y, calculator.add(x,y))

class testMult(unittest.TestCase):
    def test_random(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        self.assertEqual(x * y, calculator.mult(x,y))

    def test_zero_x(self):
        x = 0
        y = random.randint(1,10)
        self.assertEqual(0, calculator.mult(x,y))

    def test_zero_y(self):
        x = random.randint(1,10)
        y = 0
        self.assertEqual(0, calculator.mult(x,y))

class testDiv(unittest.TestCase):
        def test_random(self):
            x = random.randint(1,10)
            y = random.randint(1,10)
            self.assertEqual(x * 1.0 / y, calculator.div(x,y))

        def test_zero_x(self):
            x = 0
            y = random.randint(1,10)
            self.assertEqual(0, calculator.div(x,y))

        def test_zero_y(self):
            x = random.randint(1,10)
            y = 0
            self.assertEqual("Cannot divide by 0", calculator.div(x,y))

if __name__ == '__main__':
    unittest.main()