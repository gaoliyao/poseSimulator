from graphics import *
from Person import *
file = open("person1Frame.txt", 'r')
currWin = None
person = Person()
pose = Pose()
count = 0
for line in file:
    if "#" in line:
        win = GraphWin("window", 1000, 1000)
        pose.normalize()
        person.addPose(pose)
        pose = Pose()
        currWin = win
        count = 0
    else:
        x, y, con = line.split(" ")
        node = Node(count, int(x), int(y), con)
        pose.addNode(node)
        circle = Circle(Point(int(x), int(y)), 3)
        circle.setFill("red")
        circle.draw(currWin)
        count += 1
currWin.getMouse()
file.close()
