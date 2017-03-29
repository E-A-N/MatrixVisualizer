import modules.matrix as trix

def getMatixSize():
    '''
    This function gathers input from user to use as the size of an ideal matrix
    '''
    result = 0
    result = int(input("What size is the matrix squared?: "))
    return result

def getCoordinates():
    '''
    This function gathers inputs for user to create vectors/coordinates
    '''
    vector = {}
    question = 'y'

    while True:
        if question.lower() == "y":
            vector["x"] = int(input("What is the X coordinate"))
            vector["y"] = int(input("What is the Y coordinate"))
        else:
            break

        question = input("Do you wish to add another set of coordinates? (y or n): ")
    return vector

def main():
    running = True #main loop control
    globalXY = getMatixSize()
    #obj = getCoordinates()
    obj = {"x":0,"y":0} #create object with coordinates to work with
    #obj["preX"]
    plane = trix.cleanMatrix(globalXY)
    trix.posUpdate(plane,obj)
    while running:
      trix.pretty(plane)
      print("\n\n")
      plane = trix.cleanMatrix(globalXY)
      opt = input("WASD to move: ")
      print(opt) #debugging
      for i in "wasd":
        if i == opt:
            running = True
            break
        else:
            running = False
      opt = trix.controlListener(opt)
      trix.objAction(obj,opt,globalXY)
      trix.posUpdate(plane,obj)
    print("Program has ended!")

if __name__ == "__main__":
    main()
