import modules.matrix as trix

#constants
globalXY = 10 #matrix size


def main():
    running = True #main loop control
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
      trix.objAction(obj,opt)
      trix.posUpdate(plane,obj)
    print("Program has ended!")

if __name__ == "__main__":
    main()
