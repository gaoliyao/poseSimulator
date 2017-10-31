class Comparator:
    def dist(self, node1, node2):
        return ((float(node1.getX())-float(node2.getX()))**2 + (float(node1.getY())-float(node2.getY()))**2) ** 0.5

    def isPoseBelongsPerson(self, pose, person):
        result = 0
        poseNodes = pose.getPoseNodes()
        predictPoseNodes = person.getNextPosePrediction().getPoseNodes()
        for i in range(len(pose.getPoseNodes())):
            result += self.dist(poseNodes[i], predictPoseNodes[i])
        if result <= 1000:
            return True
        else:
            return False

    def getSmallerDistancePose(self, pose1, pose2):
        x1, y1, x2, y2 = pose1.getBound()
        a1, b1, a2, b2 = pose2.getBound()
        xAve = (x1 + x2) / 2
        aAve = (a1 + a2) / 2
        yAve = (y1 + y2) / 2
        bAve = (b1 + b2) / 2
        if (xAve**2 + yAve**2)**0.5 >= (aAve**2 + bAve**2)**0.5:
            return pose2
        else:
            return pose1
