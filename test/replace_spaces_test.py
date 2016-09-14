import unittest
import ipdb

# Write a method to replace all spaces in a string with '%20'

# I'm assuming I can't use the replace() method

def replace_spaces(string):
    chars = list(string)
    for i, char in enumerate(chars):
        if char == " ":
            last_index = len(chars) - 1
            chars[i+3:last_index+2] = chars[i+1:last_index+1]
            chars[i:i+3] = ['%','2','0']
    return ''.join(chars)

class ReplaceSpacesTest(unittest.TestCase):
    
    def test_one_space(self):
        test_string = "test string"
        expected_string = "test%20string"
        self.assertEqual(replace_spaces(test_string), expected_string)

    def test_first_char_space(self):
        test_string = " bonus"
        expected_string = "%20bonus"
        self.assertEqual(replace_spaces(test_string), expected_string)

    def test_last_char_space(self):
        test_string = "bonus "
        expected_string = "bonus%20"
        self.assertEqual(replace_spaces(test_string), expected_string)

    def test_three_consecutive_spaces(self):
        test_string = "test   string"
        expected_string = "test%20%20%20string"
        self.assertEqual(replace_spaces(test_string), expected_string)

    def test_non_consecutive_spaces(self):
        test_string = "this is how we do"
        expected_string = "this%20is%20how%20we%20do"
        self.assertEqual(replace_spaces(test_string), expected_string)

if __name__ == '__main__':
    unittest.main()
