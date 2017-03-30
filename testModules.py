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

if __name__ == "__main__":
    unittest.main()
