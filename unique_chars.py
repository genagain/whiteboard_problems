# Implement an algorithm to determin if a string has all unique characters.
# What if you can not use a additional data structures?

def unique_with_buffer(test_string):
  test_chars = list(test_string)
  unique_chars = []
  for char in test_chars:
    if char in unique_chars:
      return False
    else:
      unique_chars.append(char)
  return True

def unique_wo_buffer(test_string):
  test_chars = list(test_string)
  sorted_chars = sorted(test_chars)
  for i in range(len(sorted_chars) - 1):
    if sorted_chars[i] == sorted_chars[i+1]:
      return False
    else:
      continue
  return True
