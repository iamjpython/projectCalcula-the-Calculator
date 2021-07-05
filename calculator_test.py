import unittest
from main import Calcula

class Test(unittest.TestCase):

	def test__OO__sum(self):
		c = Calcula()
		c.input = "1 + 1"
		
		self.assertEqual(2, c.evaluate())

	def test__OO__sum_2(self):
		c = Calcula()
		c.input = "1 + 1 + 4 + 7"
		
		self.assertEqual(13, c.evaluate())

	def test__O0__difference(self):
		c = Calcula()
		c.input = "5 - 5"
		
		self.assertEqual(0, c.evaluate())

	def test__O0__difference_2(self):
		c = Calcula()
		c.input = "15 - 5 - 18"
		
		self.assertEqual(-8, c.evaluate())

	def test__O0__multiply(self):
		c = Calcula()
		c.input = "5 * 5 * 10"
		
		self.assertEqual(250, c.evaluate())

	def test__O0__divide(self):
		c = Calcula()
		c.input = "89/10"
		
		self.assertEqual(8.9, c.evaluate())

	def test_PEMDAS(self):
		c = Calcula()
		c.input = "5 + 5 - 5 * 5"
		
		self.assertEqual(-15, c.evaluate())

	def test_PEMDAS_2(self):
		c = Calcula()
		c.input = "15 + 5 - 5 * 5 / 4 + 9"
		
		self.assertEqual(22.75, c.evaluate())

	def test_PEMDAS_parenthesis(self):
		c = Calcula()
		c.input = "(((15 + 5) - 5) * 5) / ((4 + 9) + 2)"
		
		self.assertEqual(5, c.evaluate())
	
	def test__O0__square(self):
		c = Calcula()
		num = 5

		self.assertEqual(25, c.square(num))

	def test__O0__square_root(self):
		c = Calcula()
		num = 64

		self.assertEqual(8, c.square_root(num))

	def test__O0__cube(self):
		c = Calcula()
		num = 9

		self.assertEqual(729, c.cube(num))

	def test__O0__factorial(self):
		c = Calcula()
		num = 5

		self.assertEqual(120, c.factorial(num))

	def test__O0__sin(self):
		c = Calcula()
		num = 90

		self.assertEqual( 0.8939966636005579, c.sin(num))

	def test__O0__cos(self):
		c = Calcula()
		num = 0

		self.assertEqual( 1, c.cos(num))

	def test__O0__tan(self):
		c = Calcula()
		num = 0

		self.assertEqual( 0, c.tan(num))

	def test__O0__asin(self):
		c = Calcula()
		num = 1

		self.assertEqual( 1.5707963267948966, c.asin(num))

	def test__O0__acos(self):
		c = Calcula()
		num = 1

		self.assertEqual( 0, c.acos(num))

	def test__O0__atan(self):
		c = Calcula()
		num = 0

		self.assertEqual( 0, c.atan(num))

	def test__O0__log(self):
		c = Calcula()
		num = 10

		self.assertEqual( 1, c.log(num))

	def test__O0__ln(self):
		c = Calcula()
		num = 1

		self.assertEqual( 0, c.ln(num))

	
if __name__ == "__main__":
	unittest.main()
