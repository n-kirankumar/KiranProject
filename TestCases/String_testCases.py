import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('kiran'.upper(), 'KIRAN')

    def test_isupper(self):
        self.assertTrue('KIRAN'.isupper())
        self.assertFalse('kiran'.isupper())

    def test_split(self):
        s = 'Hello Kiran '
        self.assertEqual(s.split(10), ['Hello', 'Hello'])

if __name__ == '__main__':
    unittest.main()