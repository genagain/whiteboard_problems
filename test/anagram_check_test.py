import unittest
import ipdb

# Write a method to decide if two strings are anagrams or not.

def check_anagram(string1,string2):
  string1 = string1.lower().replace(' ', '')
  string2 = string2.lower().replace(' ', '')
  return char_freq(string1) == char_freq(string2)

def char_freq(string):
  chars = list(string)
  freq = {}
  for char in chars:
    if char in freq.keys():
      freq[char] += 1
    else:
      freq[char] = 1
  return freq

class TestCheckAnagram(unittest.TestCase):

  def test_anagram_wo_spaces(self):
    string1 = "Creative"
    string2 = "Reactive"
    self.assertEqual(check_anagram(string1,string2), True)

  def test_not_anagram_wo_spaces(self):
    string1 = "Bonus"
    string2 = "Reactive"
    self.assertEqual(check_anagram(string1,string2), False)

  def test_anagram_with_spaces(self):
    string1 = "Debit card"
    string2 = "Bad credit"
    self.assertEqual(check_anagram(string1,string2), True)

if __name__ == "__main__":
  unittest.main()
