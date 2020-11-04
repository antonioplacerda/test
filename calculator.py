from random import randint, randrange
import unittest

def add(numbers: str) -> int:
    if numbers == "":
        return 0

    numbers = numbers.replace('*', '')
    delimiter = ','
    numbers = numbers.replace('\n', delimiter).replace('\\n', delimiter)
    arr = (int(n) for n in numbers.split(delimiter))
    return sum(arr)

class TestStringMethods(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        rand = "78"
        self.assertEqual(add(rand), int(rand))

    def test_two_numbers(self):
        numbers = '43,67'
        self.assertEqual(add(numbers), 110)

    def test_multiple_numbers(self):
        numbers = '43,67,99,32,59,37,12,46,52,6,44,41,24,72,14,48,16,72,53,0,20,61,46,21,39,17,4,71,91,92,5,44,42,55,10,38,15,76,99,27,18,54,40,55'
        self.assertEqual(add(numbers), 1877)

    def test_new_line_delimiter(self):
        numbers = '43,67\n99,32,59,37,12,46,52\n6,44,41,24,72,14,48,16\n72,53,0,20,61,46,21\n39,17,4,71,91,92,5,44,42,55,10,38,15,76,99,27,18,54,40,55'
        self.assertEqual(add(numbers), 1877)

    def test_with_asterisk(self):
        numbers = '1\**n2**,3'
        self.assertEqual(add(numbers), 6)

if __name__ == '__main__':
    unittest.main()