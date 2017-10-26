from graphics import *
file = open("person1Frame.txt", 'r')
currWin = None
for line in file:
    if "#" in line:
        win = GraphWin("window", 1000, 1000)
        currWin = win
    else:
        x, y, con = line.split(" ")
        circle = Circle(Point(int(x), int(y)), 3)
        circle.setFill("red")
        circle.draw(currWin)
currWin.getMouse()
file.close()
