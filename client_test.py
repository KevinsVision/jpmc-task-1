import unittest
import client

class TestClient(unittest.TestCase):

    def test_getRatio(self):
        self.assertEqual(client.getRatio(10, 5), 2)
        self.assertEqual(client.getRatio(-10, 5), -2)
        self.assertEqual(client.getRatio(-10, -5), 2)

    def test_avoidZeroDivisionError(self):
        with self.assertRaises(ValueError):
            client.getRatio(10, 0)
        
        
if __name__ == '__main__':
    unittest.main()
