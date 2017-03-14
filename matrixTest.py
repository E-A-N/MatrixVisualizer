plane = []

#Don't clone arrays or Python will pass by reference!!
d1 = [0,0,0,0,0,0]
d2 = [0,0,0,0,0,0]
d3 = [0,0,0,0,0,0]
d4 = [0,0,0,0,0,0]
d5 = [0,0,0,0,0,0]

plane.append(d1)
plane.append(d2)
plane.append(d3)
plane.append(d4)
plane.append(d5)

def pretty(matrix):
    for i in matrix:
      print(i)

def xyAbstract(matrix,x,y,value):
    newMatrix = matrix
    matrix[y][x] = value
    return newMatrix

def controlListener(val):
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

def objAction(obj,act):
    xUpdate = 0
    yUpdate = 0
    if act == "up":
        yUpdate = 1
    elif act == "down":
        yUpdate = -1
    elif act == "left":
        xUpdate = -1
    elif act == "right":
        xUpdate = 1

    obj["x"] += xUpdate
    obj["y"] += yUpdate
    return obj

'''
def spacialExecution(val,matrix):
    if val = "up":
'''

obj = {"x":0,"y":0}

#pretty(plane)
#plane = xyAbstract(plane,4,4,"Hey!")
#pretty(plane)

running = True #main loop control

opt = input("Enter a character: ")
print(opt)
