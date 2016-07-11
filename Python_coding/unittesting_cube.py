def cube(n):
  """return the cube of n"""
  return n**3
def triarea(base, height):
  """return the area of triangle"""
  return base * height 
import unittest
class Mytest(unittest.TestCase):
  def test_cube(self):
    self.assertEqual(cube(5), 125)
    self.assertEqual(cube(10), 1000)
  def test_triangle(self):
    self.assertEqual(triarea(10, 20), 100)
    self.assertEqual(triarea(10, 5), 25)
unittest.main()