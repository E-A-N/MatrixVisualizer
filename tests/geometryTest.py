import unittest

def square(x):
    return x * x

def opposite(x):
    return not x

class geometryTest(unittest.TestCase):

    #Example for value
    def test_square_of_5(self):
        self.assertEqual(25,square(5),"This is not squared!")

    #Example for boolean
    def test_Opposite_Method_Of_False(self):
        self.assertTrue(opposite(False),"This is not the opposite!!")



if __name__ == "__main__":
    unittest.main()
