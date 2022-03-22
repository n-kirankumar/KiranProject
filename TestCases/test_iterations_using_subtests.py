import unittest

class NumbersTest(unittest.TestCase):


    def test_even(self):
        """tests whether the numbers between 0 and 6 are all even
        """
        for i in range(7):
            with self.subTest(i = 2 ):
                self.assertEqual(i % 2 ,0 )

