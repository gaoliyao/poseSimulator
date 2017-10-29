from poseModel.Pose import Pose
from random import randint

def createNewPose(pose1, pose2):
    newPose = Pose()
    for i in range(0, len(pose1.getPoseNodes())):
        n = randint(0, 1)
        print("ggg", i)
        if n == 0:
            newPose.addNode(pose1.getPoseNodes()[i])
        else:
            newPose.addNode(pose2.getPoseNodes()[i])
    return newPose