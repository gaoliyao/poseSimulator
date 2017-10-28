import math
from random import randint
from Node import Node
from poseModel.Pose import Pose


class Person:
    poseSequence = []
    walkingTrace = []
    nextPosePrediction = None
    currX = 0
    currY = 0
    speed = 0
    direction = 0
    poseIndex = 0
    originalAngle = 0

    def __init__(self):
        self.poseSequence = []
        self.nextPosePrediction = []
        self.currX = 0
        self.currY = 0
        self.speed = 0
        self.direction = 0
        self.poseIndex = 0
        self.walkingTrace = []
    def __init__(self, width, height):
        self.poseSequence = []
        self.nextPosePrediction = []
        self.currX =randint(int(width/5), int(width*4/5))
        self.currY = randint(int(height/5), int(height*4/5))
        self.speed = 0
        self.direction = 0
        self.poseIndex = 0
        self.walkingTrace = []
    def addPoseSequence(self, poseSequence):
        self.poseSequence = poseSequence
    def addPose(self, pose):
        self.poseSequence.append(pose)
        if len(self.poseSequence) == 1:
            self.nextPosePrediction = self.poseSequence[0]
        else:
            predictPose = Pose()
            lastPose = self.poseSequence[-1]
            lastlastPose = self.poseSequence[-2]
            for i in range(len(lastPose.getPoseNodes())):
                if i > 17:
                    break
                lastNodes = lastPose.getPoseNodes()
                lastlastNodes = lastlastPose.getPoseNodes()
                if lastNodes[i].getConfidence() != 0 and lastlastNodes[i].getConfidence() != 0:
                    node = Node(i, 2*lastNodes[i].getX() - lastlastNodes[i].getX(), 2*lastNodes[i].getY() - lastlastNodes[i].getY(), 0.5*(lastNodes[i].getConfidence() + lastlastNodes[i].getConfidence()))
                else:
                    node = Node(i, 0, 0, 0)
                predictPose.addNode(node)
            self.nextPosePrediction = predictPose
    def getNextPosePrediction(self):
        return self.nextPosePrediction
    def outputPerson(self, file):
        for pose in self.poseSequence:
            for node in pose.getPoseNodes():
                file.write(str(node.getX()) + " ")
                file.write(str(node.getY()) + " ")
                file.write(str(node.getConfidence()) + " ")
            file.write("\n")
    def getPoseSequence(self):
        return self.poseSequence
    def walk(self, speed, direction):
        dx = speed * math.cos(math.radians(direction))
        dy = speed * math.sin(math.radians(direction))
        self.currX += dx
        self.currY += dy
        newPose = Pose()
        minX, minY, maxX, maxY = newPose.getBound()
        xMean = maxX / 2
        for node in self.poseSequence[self.poseIndex % len(self.poseSequence)].getNormalizedPoseNodes():
            newNode = Node(node.getID(), self.currX + (node.getX() - xMean) * math.cos(math.radians(direction + 360 - self.originalAngle)), self.currY + node.getY() + 0.25 * (node.getX() - xMean) * math.sin(math.radians(direction + 360 - self.originalAngle)), node.getConfidence())
            newPose.addNode(newNode)
        self.walkingTrace.append(newPose)
        self.poseIndex += 1
        return newPose
    def getCurrentWalkingPose(self):
        return self.walkingTrace[self.poseIndex - 1]
    def setOriginalAngle(self, angle):
        self.originalAngle = angle
