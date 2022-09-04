import unittest

class MyTests(unittest.TestCase):
    def setUp(self):
        print('setup function')

    def tearDown(self):
        print('teardown function')

    def test_all_is_well(self):
        self.assertTrue(True, "how is this possible")

    def test_all_is_not_well(self):
        self.assertFalse(True, 'this is more like it')

if __name__ == "__main__":
    unittest.main()

