from Node import Node
from graphics import GraphWin, Circle, Point
from poseModel.Person import Person
from poseModel.Pose import Pose

file = open("person1Frame.txt", 'r')
# currWin = None
person = Person()
poseSequence = []
count = 0
index = 0
poseSequence.append(Pose())
for line in file:
    if "#" in line:
        poseSequence[index].rawNormalize()
        poseSequence.append(Pose())
        count = 0
        index += 1
    else:
        x, y, con = line.split(" ")
        node = Node(count, int(x), int(y), con)
        poseSequence[index].addNode(node)
        count += 1
person.addPoseSequence(poseSequence)
currWin = GraphWin("window", 1000, 1000)
for poseIndex in person.getPoseSequence():
    currWin = GraphWin("window", 1000, 1000)
    for node in poseIndex.getNormalizedPoseNodes():
        circle = Circle(Point(node.getX(), node.getY()), 3)
        circle.setFill("red")
        circle.draw(currWin)
currWin.getMouse()
file.close()
