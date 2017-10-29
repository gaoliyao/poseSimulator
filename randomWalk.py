from random import randint
import os

from poseModel.Pose import Pose
from utils.personLoading import loadPersonOne, loadPersonTwo

# Change the parameters here
# the number of frame
# iter time
from utils.pose import createNewPose

frameNum = 50
iterationTime = 1
cameraHeight = 100
cameraDistance = 100
viewHeight = 1080
viewWidth = 1980
minSpeed = 10
maxSpeed = 20
walkingDirectionRange = [-90, 450]

cwd = os.getcwd()

def getOverlap(x1, y1, x2, y2, x3, y3, x4, y4):
    dx = min(x2, x4) - max(x1, x3)
    dy = min(y2, y4) - max(y1, y3)
    if (dx >= 0) and (dy >= 0):
        return dx * dy / (x2 - x1) * (y2 - y1)
    else:
        return -1
def checkOcclusion(currPose):
    minX1, minY1, maxX1, maxY1 = currPose[0].getBound()
    minX2, minY2, maxX2, maxY2 = currPose[1].getBound()
    minX3, minY3, maxX3, maxY3 = currPose[2].getBound()
    oAB = 0
    oAC = 0
    oBC = 0
    if minX1 != -1:
        oAB = getOverlap(minX1, minY1, maxX1, maxY1, minX2, minY2, maxX2, maxY2)
    if minX2 != -1:
        oAC = getOverlap(minX1, minY1, maxX1, maxY1, minX3, minY3, maxX3, maxY3)
    if minX3 != -1:
        oAC = getOverlap(minX2, minY2, maxX2, maxY2, minX3, minY3, maxX3, maxY3)
    return oAB, oAC, oBC

def occlusion(currPose):
    oAB, oAC, oBC = checkOcclusion(currPose)
    if oAB != -1:
        if oAC != -1 and oBC != -1:
            currPose.remove(currPose[2])
            currPose.remove(currPose[1])
        else:
            newPose = createNewPose(currPose[0], currPose[1])
            currPose.remove(currPose[0])
            currPose.remove(currPose[0])
            currPose.append(newPose)
    elif oAC != -1:
        if oAB != -1 and oBC != -1:
            currPose.remove(currPose[2])
            currPose.remove(currPose[1])
        else:
            newPose = createNewPose(currPose[0], currPose[2])
            currPose.remove(currPose[2])
            currPose.remove(currPose[0])
            currPose.append(newPose)
    elif oBC != -1:
        if oAC != -1 and oAB != -1:
            currPose.remove(currPose[2])
            currPose.remove(currPose[1])
        else:
            newPose = createNewPose(currPose[1], currPose[2])
            currPose.remove(currPose[2])
            currPose.remove(currPose[1])
            currPose.append(newPose)
    return currPose

def getRandomRange():
    x = randint(walkingDirectionRange[0], walkingDirectionRange[1])
    y = randint(walkingDirectionRange[0], walkingDirectionRange[1])
    z = 0
    if x > y:
        z = x
        x = y
        y = z
    return x, y

out2 = open(cwd + "/data/out2.txt", "w")
out3 = open(cwd + "/data/out3.txt", "w")
start_position = (0, 0)
box_width_height = (10, 10)
moving_speed = 10
gap = 1

randomX = 0
randomY = 360

# perform random walk



for j in range(0, iterationTime):
    person1 = loadPersonOne(cwd, viewWidth, viewHeight)
    person2 = loadPersonOne(cwd, viewWidth, viewHeight)
    person3 = loadPersonOne(cwd, viewWidth, viewHeight)

    for i in range(1, frameNum + int(frameNum/10) + 1):
        currPose = []
        # person 1
        speedOne = randint(minSpeed, maxSpeed)
        directionOne = 0
        if i % 10 == 0:
            randX , randY = getRandomRange()
            directionOne += randint(randX, randY)
        person1.walk(speedOne, directionOne)
        currPoseOne = person1.getCurrentWalkingPose()
        currPose.append(currPoseOne)


        # person 2
        speedTwo = randint(minSpeed, maxSpeed)
        directionTwo = 45
        if i % 10 == 0:
            directionTwo = randint(-1, 361)
        person2.walk(speedTwo, directionTwo)
        currPoseTwo = person2.getCurrentWalkingPose()
        currPose.append(currPoseTwo)


        # person 3
        speedThree = randint(minSpeed, maxSpeed)
        directionThree = 90
        if i % 10 == 0:
            directionThree = randint(-1, 361)
        person3.walk(speedThree, directionThree)
        currPoseThree = person3.getCurrentWalkingPose()
        currPose.append(currPoseThree)

        


        minX1, minY1, maxX1, maxY1 = currPoseOne.getBound()
        if minX1 < 0 or minY1 < 0 or maxX1 >= 1980 or maxY1 >= 1080:
            out3.write("-1 -1 -1 -1 ")
            for n in currPose[0].getPoseNodes():
                n.invalid()
        else:
            out3.write(str(minX1) + " " + str(minY1) + " " + str(maxX1) + " " + str(maxY1) + " ")

        minX2, minY2, maxX2, maxY2 = currPoseTwo.getBound()
        if minX2 < 0 or minY2 < 0 or maxX2 >= 1980 or maxY2 >= 1080:
            out3.write("-1 -1 -1 -1 ")
            for n in currPose[1].getPoseNodes():
                n.invalid()
        else:
            out3.write(str(minX2) + " " + str(minY2) + " " + str(maxX2) + " " + str(maxY2) + " ")

        minX3, minY3, maxX3, maxY3 = currPoseThree.getBound()
        if minX3 < 0 or minY3 < 0 or maxX3 >= 1980 or maxY3 >= 1080:
            out3.write("-1 -1 -1 -1 ")
            for n in currPose[2].getPoseNodes():
                n.invalid()
        else:
            out3.write(str(minX3) + " " + str(minY3) + " " + str(maxX3) + " " + str(maxY3) + " ")
            
        #currPose = occlusion(currPose)

        for i in range(0, len(currPose)):
            index = randint(0, len(currPose)-1)
            for node in currPose[index].getPoseNodes():
                out2.write(str(node.getX()) + " " + str(node.getY()) + " ")
            currPose.remove(currPose[index])


        out2.write("\n")
        out3.write("\n")


out2.close()
out3.close()

inputData = open(cwd + "/data/inputData.txt", 'w')
outputData = open(cwd + "/data/outputData.txt", 'w')

out2 = open(cwd + "/data/out2.txt", 'r')
out3 = open(cwd + "/data/out3.txt", 'r')

# this is for a bug in file operations, remove unrelated lines and spaces
for line in out2:
    if line != "\n":
        inputData.write(line)

for line in out3:
    b = "100000 100000 -1 -1 100000 100000 -1 -1 100000 100000 -1 -1 " in line
    if b == False:
        outputData.write(line)
# ***********************************************************************

inputData.close()
outputData.close()
