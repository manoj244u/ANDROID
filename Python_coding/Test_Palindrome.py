import unittest
from isPalindromes import isPalidrome
class PalindromeTestCase(unittest.TestCase):
  """ test for Palindrome """
  def test_Palindrome():
    assertTrue(isPalidrome())
if __name__ == '__main__':
  unittest.main()