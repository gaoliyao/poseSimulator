from poseModel.Node import Node
from poseModel.Person import Person
from poseModel.Pose import Pose
from poseModel.graphics import GraphWin, Circle, Point

file = open("/data/person2Frame.txt", 'r')
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
currWin = GraphWin("window", 100, 100)
for poseIndex in person.getPoseSequence():
    currWin = GraphWin("window", 100, 100)
    for node in poseIndex.getNormalizedPoseNodes():
        circle = Circle(Point(0 + node.getX(), node.getY()), 3)
        circle.setFill("red")
        circle.draw(currWin)
    currWin.getMouse()

file.close()

