#python has assertion
a = 5
assert a > 0
#assert a < 0 #assertion error 
#for sanity check, not for (user input)validation or production code

#in order to write unit test, we need to write a series of assertion 
def multiply(x, y):
	return x + y

#usually tests live in a test file or module, not inline
import unittest
#this signifies it contains a series of unit tests
#making a sub test class with unittest.TestCase
class TestMultiply(unittest.TestCase):
	#unit test needs to start with test_
	def test_multiply(self):
		test_x = 5
		test_y = 10 

		self.assertEqual(multiply(test_x, test_y), 50, "should be 50")

if __name__ == "__main__": #if I run this file directory
	unittest.main() #then call this method 
#if I were to remove main then I can do
#python -m unittest testing