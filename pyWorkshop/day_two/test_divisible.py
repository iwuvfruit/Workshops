import unittest
from divisible import divisible_by

#sub class of unittest
class DivisibleTestCase(unittest.TestCase):
	#start with test_
	def test_divisible_by(self):
		self.assertTrue(divisible_by(10, 2))
		self.assertFalse(divisible_by(10, 3))

	#I can run multiple tests
if __name__ == '__main__':
	unittest.main()

#python test_divisible.py --verbose to see exactly which test case ran

#if no main then 
#python -m unittest test_divisible