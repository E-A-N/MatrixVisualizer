'''
    This module
'''

def slope(p1,p2):
    '''
    This function calculates the slope of a given 2
    points.
    :type p1: list
    :param p1: 1st pair of xy coordinates
    :type p2: list
    :param p2: 2nd pair of xy coordinates
    '''
    #y is index 0, x is index 1
    slope = []
    slope.append(p2[0] - p1[0])
    slope.append(p2[1] - p1[1])

    return slope
