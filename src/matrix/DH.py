import math


class DH:

    def __init__(self, d, theta, a, alpha):
        self.d = d
        self.theta = theta
        self.a = a
        self.alpha = alpha

        self.matrix = []
        self.updateMatrix()

    def updateMatrix(self):
        self.matrix = [[math.cos(self.theta), -1.0 * math.sin(self.theta) * math.cos(self.alpha), math.sin(self.theta) * math.sin(self.alpha), self.a * math.cos(self.theta)],
                       [math.sin(self.theta), math.cos(self.theta) * math.cos(self.alpha), -1.0 * math.cos(self.theta) * math.sin(self.alpha), self.a * math.sin(self.theta)],
                       [0.0, math.sin(self.alpha), math.cos(self.alpha), self.d],
                       [0.0, 0.0, 0.0, 1.0]]

    def setD(self, d):
        self.d = d
        self.updateMatrix()

    def setTheta(self, theta):
        self.theta = theta
        self.updateMatrix()

    def setA(self, a):
        self.a = a
        self.updateMatrix()

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.updateMatrix()

    def clone(self):
        return DH(self.d, self.theta, self.a, self.alpha)

    def printString(self, id):
        print("dh" + str(id) + "_theta = ", self.theta)
        print("dh" + str(id) + "_d = ", self.d/1000.0)
        print("dh" + str(id) + "_a = ", self.a/1000.0)
        print("dh" + str(id) + "_alpha = ", self.alpha)
        # print("ID:", id, "D:", self.d, "Theta:", self.theta, "A:", self.a, "Alpha:", self.alpha)

    def printDHLink(self):
        print("self.dhSegments.append(DHSegment(" + str(self.theta) + " ," + str(self.d) + " ," + str(self.a) + " ," + str(self.alpha) + "))")
