from Node import Node
from Pose import Pose


class Person:
    poseSequence = []
    nextPosePrediction = None

    def __init__(self):
        self.poseSequence = []
        self.nextPosePrediction = []
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
