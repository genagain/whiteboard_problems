import unittest

# Design an algorithm and write code to remove the duplicate characters in a string
# without using an additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.

def remove_dup_chars(test_string):
  unique_chars = ""
  for char in list(test_string):
    if char not in unique_chars:
      unique_chars += char
  return unique_chars

class TestRemoveDupChars(unittest.TestCase):

  def test_unique_input(self):
    test_string = "python"
    self.assertEqual(remove_dup_chars(test_string), test_string)

  def test_non_unique_input(self):
    test_string = "aabbbdddeefffgggjjjjjiiikkk"
    unique_chars = "abdefgjik"
    self.assertEqual(remove_dup_chars(test_string), unique_chars)

if __name__ == '__main__':
  unittest.main()
