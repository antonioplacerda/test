import unittest

def add():
    pass

class TestStringMethods(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(), 0)

if __name__ == '__main__':
    unittest.main()