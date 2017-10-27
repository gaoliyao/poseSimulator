from Comparator import Comparator
from Node import Node
from Person import Person
from Pose import Pose

file = open("data.txt", 'r')
output = []
output = open("output.txt", 'w')
person = []
comparator = Comparator()

def existPerson(pose):
    if len(person) == 0:
        return False
    else:
        for p in person:
            if comparator.isPoseBelongsPerson(pose, p):
                return p
        return False


for line in file:
    line.replace("\n", "")
    numbers = line.split(" ")
    for i in range(1, len(numbers), 54):
        pose = Pose()
        count = 0
        for j in range(i, i + 54, 3):
            if j + 2 > len(numbers)-1:
                break
            print(count, numbers[j], numbers[j+1], numbers[j+2])
            pose.addNode(Node(count, float(numbers[j]), float(numbers[j+1]), float(numbers[j+2])))
            count += 1
        if pose.getAveConfidence() >= 0.4:
            if existPerson(pose) != False:
                existPerson(pose).addPose(pose)
            else:
                newPerson = Person()
                newPerson.addPose(pose)
                person.append(newPerson)
for i in range(len(person)):
    output.write(str(i) + "\n")
    person[i].outputPerson(output)
file.close()
output.close()

