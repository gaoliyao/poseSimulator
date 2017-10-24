class Comparator:
    def dist(self, node1, node2):
        return ((float(node1.getX())-float(node2.getX()))**2 + (float(node1.getY())-float(node2.getY()))**2) ** 0.5

    def isPoseBelongsPerson(self, pose, person):
        result = 0
        poseNodes = pose.getPoseNodes()
        predictPoseNodes = person.getNextPosePrediction().getPoseNodes()
        for i in range(len(pose.getPoseNodes())):
            result += self.dist(poseNodes[i], predictPoseNodes[i])
        if result <= 0.001:
            return True
        else:
            return False