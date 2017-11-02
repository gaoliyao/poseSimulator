from poseModel.Node import Node
from poseModel.graphics import *
class Pose:
    poseNodes = []
    normalizedPoseNodes = []
    showPoints = []
    AveConfidence = 0.0
    minX = 100000
    maxX = -1
    minY = 100000
    maxY = -1
    noisePoseNodes = []
    def __init__(self):
        self.poseNodes = []
        self.normalizedPoseNodes = []
        self.noisePoseNodes = []
        self.showPoints = []
        self.AveConfidence = 0.0
        self.minX = 100000
        self.maxX = -1
        self.minY = 100000
        self.maxY = -1
    def addNode(self, node):
        self.poseNodes.append(node)
    def getAveConfidence(self):
        count = len(self.poseNodes)
        if count == 0:
            return 0
        sum = 0
        for p in self.poseNodes:
            sum += p.getConfidence()
        return sum / count
    def show(self, win):
        for p in self.poseNodes:
            c = Circle(Point(p.getX(), p.getY()), 3)
            self.showPoints.append(c)
            c.draw(win)
    def unshow(self, win):
        for p in self.showPoints:
            p.undraw()
    def getPoseNodes(self):
        return self.poseNodes[0: len(self.poseNodes)]
    def rawNormalize(self):
        for node in self.poseNodes:
            if node.getX() < self.minX:
                self.minX = node.getX()
            if node.getY() < self.minY:
                self.minY = node.getY()
        for node in self.poseNodes:
            newNode = node
            newNode.normalize(self.minX, self.minY, 1)
            self.normalizedPoseNodes.append(newNode)
    def normalize(self, height):

        for node in self.poseNodes:
            if node.getX() > self.maxX:
                self.maxX = node.getX()
            if node.getX() < self.minX:
                self.minX = node.getX()
            if node.getY() > self.maxY:
                self.maxY = node.getY()
            if node.getY() < self.minY:
                self.minY = node.getY()
        for node in self.poseNodes:
            newNode = node
            newNode.normalize(self.minX, self.minY, (self.maxY-self.minY) / height)
            self.normalizedPoseNodes.append(newNode)
    def getNormalizedPoseNodes(self):
        return self.normalizedPoseNodes
    def getBound(self):
        for node in self.poseNodes:
            if node.getX() > self.maxX:
                self.maxX = node.getX()
            if node.getX() < self.minX:
                self.minX = node.getX()
            if node.getY() > self.maxY:
                self.maxY = node.getY()
            if node.getY() < self.minY:
                self.minY = node.getY()
        return self.minX, self.minY, self.maxX, self.maxY
    def addMovedNoise(self):
        nodeList = []
        for node in self.getPoseNodes():
            newNode = Node(node.getID(), node.getX() / (1 + (50 / node.getX())), node.getY() / (1 + (50 / node.getY())), node.getConfidence())
            nodeList.append(newNode)
        self.noisePoseNodes = nodeList
    def isNoiseExist(self):
        if len(self.noisePoseNodes) == 0:
            return False
        else:
            return True
    def getNoisePoseNodes(self):
        return self.noisePoseNodes