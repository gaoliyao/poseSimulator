from random import randint

from Node import Node
from Person import Person
from Pose import Pose


def loadPersonOne():
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



out = open("out2.txt","w")
start_position = (0,0)
box_width_height = (10,10)
moving_speed = 10
gap = 1
person1 = loadPersonOne()
person2 = loadPersonOne()
person3 = loadPersonOne()

# Write the first data
for i in range(1, 11):
    # person 1
    speedOne = randint(10, 20)
    person1.walk(speedOne, 90)
    currPoseOne = person1.getCurrentWalkingPose()
    for node in currPoseOne.getPoseNodes():
        out.write(str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " ")
    # person 2
    speedTwo = randint(10, 20)
    person2.walk(speedTwo, 45)
    currPoseTwo = person2.getCurrentWalkingPose()
    for node in currPoseTwo.getPoseNodes():
        out.write(str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " ")
    # person 3
    speedThree = randint(10, 20)
    person3.walk(speedThree, 0)
    currPoseThree = person3.getCurrentWalkingPose()
    for node in currPoseThree.getPoseNodes():
        out.write(str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " ")
    out.write("\n")
# Generate horizontal moving box
# loop_p = start_position
# for i in range(1,11):
#     moving_speed = randint(10,20)
#     (tmp_x,tmp_y) = loop_p
#     tmp_x += moving_speed + gap
#     person = loadPersonOne()
#     currPose = person.getPoseSequence()[i % len(person.getPoseSequence())]
#     outputStr = "0 " + "frame" + str(i) + " "
#     for node in currPose.getPoseNodes():
#         node.normalize(-tmp_x, -tmp_y, 5)
#         outputStr += str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " "
#     out.write(outputStr + "\n")
#     loop_p = (tmp_x,tmp_y)
#
# # Generate vertical moving box
# loop_p = start_position
# for i in range(1,11):
#     moving_speed = randint(10,20)
#     (tmp_x,tmp_y) = loop_p
#     tmp_y += moving_speed + gap
#     person = loadPersonOne()
#     currPose = person.getPoseSequence()[i % len(person.getPoseSequence())]
#     outputStr = "1 " + "frame" + str(i) + " "
#     for node in currPose.getPoseNodes():
#         node.normalize(-tmp_x, -tmp_y, 5)
#         outputStr += str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " "
#     out.write(outputStr + "\n")
#     loop_p = (tmp_x, tmp_y)
#
# # Generate diagonal moving box
# moving_speed = 14
# loop_p = start_position
# for i in range(1,11):
#     moving_speed = randint(14,20)
#     (tmp_x,tmp_y) = loop_p
#     tmp_x += moving_speed + gap
#     tmp_y += moving_speed + gap
#     person = loadPersonOne()
#     currPose = person.getPoseSequence()[i % len(person.getPoseSequence())]
#     outputStr = "2 " + "frame" + str(i) + " "
#     for node in currPose.getPoseNodes():
#         node.normalize(-tmp_x, -tmp_y, 5)
#         outputStr += str(node.getX()) + " " + str(node.getY()) + " " + str(node.getConfidence()) + " "
#     out.write(outputStr + "\n")
#     loop_p = (tmp_x, tmp_y)

out.close()
