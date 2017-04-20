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

def abs(num):
    '''
    This function gets the absolute value of a given number.
    :type num: int
    :param num: The number to check if it's positive
    '''
    val = num
    if val < 0:
        val = val * -1
    return val

def reduce(slope):
    '''
    This function simplifys the value of a slope down to it's
    greatest common factors
    '''
    newSlope = slope
    div0 = newSlope[0] % 2
    div1 = newSlope[1] % 2
    while ((div0 == 0) and (div1 == 0)):
        newSlope[0] /= 2
        newSlope[1] /= 2
        div0 = newSlope[0] % 2
        div1 = newSlope[1] % 2

    return newSlope

def increaseAccuracy(slope):
    '''
    This function reduces slopes coordinates while they're
    not floating point values
    :type slope: list
    :param slope: The sloop to reduce
    '''
    zoomed = slope #use insert reduced/accurate data
    prePoints = slope
    y = slope[0]
    x = slope[1]
    maxAccuracy = False
    while True:
        y = abs(y)
        x = abs(x)
        print(y)
        if ((type(y/2) == int) and (type(x/2) == int)):
            zoomed[0] = y/2
            zoomed[1] = x/2
            y = zoomed[0]
            x = zoomed[1]
        else:
            break

    return zoomed

#slo = slope([8,2], [2,8])
#print(slo)
#accSlo = increaseAccuracy(slo)
#print(accSlo)
