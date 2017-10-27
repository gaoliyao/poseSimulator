from random import randint

from Node import Node
from Person import Person
from Pose import Pose

cameraHeight = 100
cameraDistance = 100

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



inputData = open("out2.txt","w")
outputData = open("out3.txt","w")
start_position = (0,0)
box_width_height = (10,10)
moving_speed = 10
gap = 1
person1 = loadPersonOne()
person2 = loadPersonOne()
person3 = loadPersonOne()

# Write the first data
for i in range(1, 101):
    # person 1
    speedOne = randint(10, 20)
    directionOne = 0
    if i % 10 == 0:
        directionOne = randint(-1, 361)
    person1.walk(speedOne, directionOne)
    currPoseOne = person1.getCurrentWalkingPose()
    minX, minY, maxX, maxY = currPoseOne.getBound()
    outputData.write(str(minX) + " " + str(minY) + " " + str(maxX) + " " + str(maxY) + " ")
    for node in currPoseOne.getPoseNodes():
        inputData.write(str(node.getX()) + " " + str(node.getY()) + " ")

    # person 2
    speedTwo = randint(10, 20)
    directionTwo = 45
    if i % 10 == 0:
        directionTwo = randint(-1, 361)
    person2.walk(speedTwo, directionTwo)
    currPoseTwo = person2.getCurrentWalkingPose()
    minX, minY, maxX, maxY = currPoseTwo.getBound()
    outputData.write(str(minX) + " " + str(minY) + " " + str(maxX) + " " + str(maxY) + " ")
    for node in currPoseTwo.getPoseNodes():
        inputData.write(str(node.getX()) + " " + str(node.getY()) + " ")

    # person 3
    speedThree = randint(10, 20)
    directionThree = 90
    if i % 10 == 0:
        directionThree = randint(-1, 361)
    person3.walk(speedThree, directionThree)
    currPoseThree = person3.getCurrentWalkingPose()
    minX, minY, maxX, maxY = currPoseThree.getBound()
    outputData.write(str(minX) + " " + str(minY) + " " + str(maxX) + " " + str(maxY) + " ")
    for node in currPoseThree.getPoseNodes():
        inputData.write(str(node.getX()) + " " + str(node.getY()) + " ")

    inputData.write("\n")
    outputData.write("\n")
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

inputData.close()
outputData.close()
