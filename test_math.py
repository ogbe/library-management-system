import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)

if __name__ == "__main__":
    unittest.main()