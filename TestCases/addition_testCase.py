import unittest

def sub(a,b):
    return a-b


class SimpleTest(unittest.TestCase):
    def test_subfun(self):
        self.assertEquals(10, sub(0, 2))

if __name__ == '__main__':
    unittest.main()