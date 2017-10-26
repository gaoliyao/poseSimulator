from graphics import *
class Pose:
    poseNodes = []
    normalizedPoseNodes = []
    showPoints = []
    AveConfidence = 0.0
    def __init__(self):
        self.poseNodes = []
        self.normalizedPoseNodes = []
        self.showPoints
        self.AveConfidence = 0.0
    def addNode(self, node):
        self.poseNodes.append(node)
    def getAveConfidence(self):
        count = len(self.poseNodes)
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
        return self.poseNodes
    def normalize(self):
        minX = 100000
        minY = 100000
        for node in self.poseNodes:
            if node.getX() < minX:
                minX = node.getX()
            if node.getY() < minY:
                minY = node.getY()
        for node in self.poseNodes:
            newNode = node
            newNode.normalize(minX, minY)
            self.normalizedPoseNodes.append(newNode)
    def getNormalizedPoseNodes(self):
        return self.normalizedPoseNodes