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

def controls(val):
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

def objAction(val):
    if val = 

#pretty(plane)
plane = xyAbstract(plane,4,4,"Hey!")
pretty(plane)

running = True

opt = input("Enter a character: ")
print(opt)
