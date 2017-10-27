from Node import Node
from Person import Person
from Pose import Pose
from graphics import GraphWin, Circle, Point

file = open("person2Frame.txt", 'r')
# currWin = None
person = Person()
poseSequence = []
count = 0
index = 0
poseSequence.append(Pose())
for line in file:
    line = line.replace("\n", "")
    if "#" in line:
        poseSequence[index].rawNormalize()
        poseSequence.append(Pose())
        count = 0
        index += 1
    else:
        print(line)
        x, y, con = line.split(" ")
        node = Node(count, int(x), int(y), con)
        poseSequence[index].addNode(node)
        count += 1
person.addPoseSequence(poseSequence)
currWin = GraphWin("window", 1000, 1000)
for poseIndex in person.getPoseSequence():
    currWin = GraphWin("window", 1000, 1000)
    for node in poseIndex.getNormalizedPoseNodes():
        circle = Circle(Point(900 + node.getX(), node.getY()), 3)
        circle.setFill("red")
        circle.draw(currWin)
currWin.getMouse()
file.close()

