from poseModel.Node import Node
from poseModel.Person import Person
from poseModel.Pose import Pose
from poseModel.graphics import GraphWin, Circle, Point

def loadPersonOne(cwd, viewWidth, viewHeight):
    file = open(cwd + "/data/person1Frame.txt", 'r')
    # currWin = None
    person = Person(viewWidth, viewHeight)
    poseSequence = []
    count = 0
    index = 0
    person.setOriginalAngle(225)
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
    file.close()
    return person


def loadPersonTwo(cwd, viewWidth, viewHeight):
    file = open(cwd + "/data/person2Frame.txt", 'r')
    # currWin = None
    person = Person(viewWidth, viewHeight)
    person.setOriginalAngle(120)
    poseSequence = []
    count = 0
    index = 0
    poseSequence.append(Pose())
    for line in file:
        line = line.replace("\n", "")
        if "#" in line:
            poseSequence[index].rawNormalize()
            poseSequence.append(Pose())
            count = 0
            index += 1
        else:
            print(line)
            x, y, con = line.split(" ")
            node = Node(count, int(x), int(y), con)
            poseSequence[index].addNode(node)
            count += 1
    person.addPoseSequence(poseSequence)
    file.close()
    return person