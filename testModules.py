import unittest
import random
import modules.geometry as geo
import modules.matrix as trix

class geometrySlopeTest(unittest.TestCase):

    def test_slope_neg6_6(self):
        slope = geo.slope([8,2],[2,8])
        self.assertEqual([-6,6],slope,"Incorrect slope value")

    def test_slope_10_neg14(self):
        slope = geo.slope([-4,9],[6,-5])
        self.assertEqual([10,-14],slope,"Incorrect slope value")

    def test_slope_positive_odds_7931(self):
        slope = geo.slope([7,9],[3,1])
        self.assertEqual([-4,-8],slope,"Incorrect slope value")

    def test_slope_negative_odds_133296(self):
        slope = geo.slope([-13,-3],[-29,-6])
        self.assertEqual([-16,-3],slope,"Incorrect slope value")

    '''
    def test_slope_random_values(self):
        cap = 100
        x1 = random.randint(-cap,cap)
        y1 = random.randint(-cap,cap)
        x2 = random.randint(-cap,cap)
        y2 = random.randint(-cap,cap)
        slope = geo.slope([x1,y1],[x2,y2])
    '''

    def test_slope_data_type(self):
        slope = geo.slope([-4,9],[6,-5])
        slopeType = type(slope) == list
        self.assertTrue(slopeType, "This is not a list type!")

    ###ABSOLUTE VALUE TESTS###
    def test_absolute_value_neg99(self):
        val = geo.abs(-99)
        test = val > 0
        statement = "%d is not positive ----- val > 0 is %s" % (val,test)
        self.assertTrue(test, statement)

    def test_absolute_vale_neg5(self):
        val = geo.abs(-5)
        self.assertEqual(5,val, "The absolute value of -5 is 5 not %d" %(val))

    def test_absolute_value_7(self):
        val = geo.abs(7)
        test = val > 0
        statement = "%d is not positive ----- val > 0 is %s" % (val,test)
        self.assertTrue(test, statement)

    ###SIMPLIFY TESTS###
    def test_reduce_of_8_2(self):
        slope = geo.reduce([8,2])
        testValue =  [4,1]
        self.assertEqual(testValue, slope, "Incorrect value")

if __name__ == "__main__":
    unittest.main()
