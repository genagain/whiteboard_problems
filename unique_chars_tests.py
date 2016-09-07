import unittest
import unique_chars

# Implement an algorithm to determin if a string has all unique characters.
# What if you can not use a additional data structures?
class TestUniqueChars(unittest.TestCase):

  def test_not_unique_with_buffer(self):
    test_string = "test string"
    self.assertEqual(unique_chars.unique_with_buffer(test_string), False)

  def test_unique_with_buffer(self):
    test_string = "python"
    self.assertEqual(unique_chars.unique_with_buffer(test_string), True)

  def test_not_unique_wo_buffer(self):
    test_string = "test string"
    self.assertEqual(unique_chars.unique_wo_buffer(test_string), False)

  def test_unique_wo_buffer(self):
    test_string = "python"
    self.assertEqual(unique_chars.unique_wo_buffer(test_string), True)

if __name__ == '__main__':
  unittest.main()
