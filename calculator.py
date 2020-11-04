from random import randint, randrange
import unittest

def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ','
    numbers = numbers.replace('\n', delimiter)
    arr = (int(n) for n in numbers.split(delimiter))
    return sum(arr)

class TestStringMethods(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        rand = randrange(100)
        self.assertEqual(add(str(rand)), rand)

    def test_two_numbers(self):
        rand = [randrange(100) for _ in range(2)]
        numbers = ','.join((str(r) for r in rand))
        self.assertEqual(add(numbers), sum(rand))

    def test_multiple_numbers(self):
        rand = [randrange(100) for _ in range(randint(3, 50))]
        numbers = ','.join((str(r) for r in rand))
        self.assertEqual(add(numbers), sum(rand))

    def test_new_line_delimiter(self):
        rand = [randrange(100) for _ in range(randint(3, 50))]
        numbers = '\n'.join((str(r) for r in rand))
        self.assertEqual(add(numbers), sum(rand))

if __name__ == '__main__':
    unittest.main()