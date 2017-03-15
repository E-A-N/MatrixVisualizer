def cleanMatrix(num):
    mat=[]
    for y in range(num):
        mat.append([])
        for x in range(num):
          mat[y].append(x)
          mat[y][x] = 0
    return mat

plane = cleanMatrix(6)


def pretty(matrix):
    for i in matrix:
      print(i)

pretty(plane)

def xyAbstract(matrix,x,y,value):
    newMatrix = matrix
    matrix[y][x] = value
    #return newMatrix
    
def posUpdate(matrix,obj):
    pos = "XX"
    x = obj["x"]
    y = obj["y"]
    matrix[x][y] = pos


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

'''
running = True #main loop control
obj = {"x":0,"y":0}
#obj["preX"]
posUpdate(plane,obj)
while running:
  pretty(plane)
  cleanMatrix(plane)
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
'''





