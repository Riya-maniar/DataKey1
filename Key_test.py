import unittest
import Riya_key

class KeyTest(unittest.TestCase):

    def test_zero(self):
        result = Riya_key.safe_key()
        self.assertNotEqual(result,None)

if __name__ == '__main__':
    unittest.main()
