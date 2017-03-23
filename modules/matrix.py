#constants
globalXY = 10 #matrix size

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

def objAction(obj,act,boundary = globalXY):
    '''
    This function enables objects to exectue an action
    :type obj: dict
    :param obj: object to append actions to
    :type act: string
    :param act: action for object to execute
    '''
    topBound = (boundary - 1) * -1
    xBound = boundary - 1
    xUpdate = 0
    yUpdate = 0
    if ((act == "up") and (obj["y"] < topBound)):
        yUpdate = -1
    elif act == "down":
        yUpdate = 1
    elif act == "left":
        xUpdate = -1
    elif act == "right":
        xUpdate = 1

    obj["x"] += xUpdate
    obj["y"] += yUpdate


'''
def main():
    running = True #main loop control
    obj = {"x":0,"y":0} #create object with coordinates to work with
    #obj["preX"]
    plane = cleanMatrix(globalXY)
    posUpdate(plane,obj)
    while running:
      pretty(plane)
      print("\n\n")
      plane = cleanMatrix(globalXY)
      opt = input("WASD to move: ")
      print(opt) #debugging
      for i in "wasd":
        if i == opt:
            running = True
            break
        else:
            running = False
      opt = controlListener(opt)
      objAction(obj,opt)
      posUpdate(plane,obj)
    print("Program has ended!")

if __name__ == "__main__":
    main()
'''
