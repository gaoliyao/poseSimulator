from random import randint

from poseModel.Node import Node
from poseModel.Person import Person
from poseModel.Pose import Pose


def loadPersonOne():
    file = open("/data/person1Frame.txt", 'r')
    # currWin = None
    person = Person()
    poseSequence = []
    count = 0
    index = 0
    poseSequence.append(Pose())
    for line in file:
        if "#" in line:
            poseSequence[index].Normalize(10)
            poseSequence.append(Pose())
            count = 0
            index += 1
        else:
            x, y, con = line.split(" ")
            node = Node(count, int(x), int(y), con)
            poseSequence[index].addNode(node)
            count += 1
    person.addPoseSequence(poseSequence)
    # currWin = GraphWin("window", 1000, 1000)
    # for poseIndex in person.getPoseSequence():
    #     currWin = GraphWin("window", 1000, 1000)
    #     for node in poseIndex.getNormalizedPoseNodes():
    #         circle = Circle(Point(node.getX(), node.getY()), 3)
    #         circle.setFill("red")
    #         circle.draw(currWin)
    # currWin.getMouse()
    file.close()
    return person



out = open("/data/out.txt","w")
start_position = (0,0)
box_width_height = (10,10)
moving_speed = 10
gap = 1
# Write the first data
out.write("{} {} {} {} {}\n".format(0,start_position[0],start_position[1],box_width_height[0],box_width_height[1]))

# Generate horizontal moving box
loop_p = start_position
for i in range(1,11):
    moving_speed = randint(10,20)
    (tmp_x,tmp_y) = loop_p
    tmp_x += moving_speed + gap
    person = loadPersonOne()
    currPose = person.getPoseSequence()[i % len(person.getPoseSequence())]
    outputStr = "0 " + "frame" + str(i) + " "
    for node in currPose.getPoseNodes():
        node.normalize(-tmp_x, -tmp_y, 5)
        outputStr += str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " "
    out.write(outputStr + "\n")
    loop_p = (tmp_x,tmp_y)

# Generate vertical moving box
loop_p = start_position
for i in range(1,11):
    moving_speed = randint(10,20)
    (tmp_x,tmp_y) = loop_p
    tmp_y += moving_speed + gap
    person = loadPersonOne()
    currPose = person.getPoseSequence()[i % len(person.getPoseSequence())]
    outputStr = "1 " + "frame" + str(i) + " "
    for node in currPose.getPoseNodes():
        node.normalize(-tmp_x, -tmp_y, 5)
        outputStr += str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " "
    out.write(outputStr + "\n")
    loop_p = (tmp_x, tmp_y)

# Generate diagonal moving box
moving_speed = 14
loop_p = start_position
for i in range(1,11):
    moving_speed = randint(14,20)
    (tmp_x,tmp_y) = loop_p
    tmp_x += moving_speed + gap
    tmp_y += moving_speed + gap
    person = loadPersonOne()
    currPose = person.getPoseSequence()[i % len(person.getPoseSequence())]
    outputStr = "2 " + "frame" + str(i) + " "
    for node in currPose.getPoseNodes():
        node.normalize(-tmp_x, -tmp_y, 5)
        outputStr += str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " "
    out.write(outputStr + "\n")
    loop_p = (tmp_x, tmp_y)

out.close()
