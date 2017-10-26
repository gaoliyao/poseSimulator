class Node:
    x = 0
    y = 0
    confidence = 0.0
    id = -1
    name = ""
    nameList = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "RHip", "RKnee",
                "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "Background"]
    def __init__(self, id):
        self.x = 0
        self.y = 0
        self.confidence = 0.0
        self.id = id
        self.name = self.nameList[id]
    def __init__(self, id, x, y, confidence):
        self.x = float(x)
        self.y = float(y)
        self.confidence = float(confidence)
        self.id = id
        print(id)
        self.name = self.nameList[id]
    def rawNormalize(self, lengthX, lengthY):
        self.x -= lengthX
        self.y -= lengthY
    def normalize(self, lengthX, lengthY, scale):
        self.x /= scale
        self.y /= scale
        self.x -= lengthX
        self.y -= lengthY
    def getConfidence(self):
        return self.confidence
    def getX(self):
        return round(self.x, 6)
    def getY(self):
        return round(self.y, 6)
    def getID(self):
        return self.id
