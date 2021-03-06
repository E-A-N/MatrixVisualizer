def cleanMatrix(num):
    '''
    This function creates a matrix the size of num^2
    '''
    mat=[]
    for y in range(num):
        mat.append([])
        for x in range(num):
          mat[y].append(x)
          mat[y][x] = 0
    return mat

def pretty(matrix):
    '''
    This function prints a matrix in a readable format
    :type matrix: list
    :param matrix: plane to be displayed
    '''
    for i in matrix:
      print(i)

def posUpdate(matrix,obj):
    '''
    This function interfaces an objects coordinates with a plane
    :type matrix: list
    :param matrix: plane to be updated
    :type obj: dict
    :param obj: this object will provide coordinates for the plane
    '''
    pos = "X"
    x = obj["x"]
    y = obj["y"]
    matrix[y][x] = pos


def controlListener(val):
    '''
    This takes input to generate action.
    :type val: string
    :param val: character codes from input
    '''
    action = ''
    if val == "w":
        action = "up"
    elif val == "s":
        action = "down"
    elif val == "a":
        action = "left"
    elif val == "d":
        action = "right"
    return action

def objAction(obj,act,boundary):
    '''
    This function transaltes coordinates to a new position in the matrix
    :type obj: dict
    :param obj: object to append actions to
    :type act: string
    :param act: action for object to execute
    '''
    topBound = (boundary - 1) #* -1
    xBound = boundary - 1
    xUpdate = 0
    yUpdate = 0
    print(topBound) #for debugging
    print(obj["y"]) #for debugging
    if ((act == "up") and (obj["y"] > 0)): #0 is ground level
        yUpdate = -1
    elif ((act == "down") and (obj["y"] < topBound)):
        yUpdate = 1
    elif ((act == "left") and (obj["x"] > 0)):
        xUpdate = -1
    elif ((act == "right") and (obj["x"] < boundary - 1)):
        xUpdate = 1

    obj["x"] += xUpdate
    obj["y"] += yUpdate
