import math

import transformations

import numpy

class Quaternion:

    def __init__(self, q, x=0, y=0, z=0):
        if q is not None:
            self.q = q
            self.matrix = [[(self.q[0] * self.q[0] + self.q[1] * self.q[1]) - (self.q[2] * self.q[2] + self.q[3] * self.q[3]),
                            2.0 * (self.q[1] * self.q[2] - self.q[0] * self.q[3]),
                            2.0 * (self.q[0] * self.q[2] + self.q[1] * self.q[3]), 0.0],
                           [2.0 * (self.q[1] * self.q[2] + self.q[0] * self.q[3]),
                            (self.q[0] * self.q[0] + self.q[2] * self.q[2]) - (self.q[1] * self.q[1] + self.q[3] * self.q[3]),
                            2.0 * (self.q[2] * self.q[3] - self.q[0] * self.q[1]), 0.0],
                           [2.0 * (self.q[1] * self.q[3] - self.q[0] * self.q[2]),
                            2.0 * (self.q[0] * self.q[1] + self.q[2] * self.q[3]),
                            (self.q[0] * self.q[0] + self.q[3] * self.q[3]) - (self.q[1] * self.q[1] + self.q[2] * self.q[2]), 0.0],
                           [0.0, 0.0, 0.0, 1.0]]
        else:
            d = math.sqrt(x*x + y*y + z*z)
            I3 = [[1.0, 0, 0], [0, 1, 0], [0, 0, 1]]
            k = [[0, -1.0*z, y], [z, 0, -1.0*x], [-1.0*y, x, 0]]
            R3 = I3 + numpy.dot(math.sin(d), k) + numpy.dot((1.0-math.cos(d)), numpy.matmul(k, k))
            self.matrix = [[R3[0][0], R3[0][1], R3[0][2], 0.0],
                           [R3[1][0], R3[1][1], R3[1][2], 0.0],
                           [R3[2][0], R3[2][1], R3[2][2], 0.0],
                           [0.0, 0.0, 0.0, 1.0]]
            
            self.q = transformations.quaternion_from_matrix(self.matrix)

    def getQ0(self):
        return self.q[0]

    def getQ1(self):
        return self.q[1]

    def getQ2(self):
        return self.q[2]

    def getQ3(self):
        return self.q[3]

    def getYaw(self):
        return math.atan2(2.0*(self.q[2]*self.q[3] + self.q[0]*self.q[1]),
                          self.q[0]*self.q[0] - self.q[1]*self.q[1] - self.q[2]*self.q[2] + self.q[3]*self.q[3])

    def getPitch(self):
        return math.asin(-2.0*(self.q[1]*self.q[3] - self.q[0]*self.q[2]));

    def getRoll(self):
        return math.atan2(2.0*(self.q[1]*self.q[2] + self.q[0]*self.q[3]),
                          self.q[0]*self.q[0] + self.q[1]*self.q[1] - self.q[2]*self.q[2] - self.q[3]*self.q[3])
    
    def getRPY(self):
        return [self.getRoll(), self.getPitch(), self.getYaw()]


    def getAngle(self):
        return 2 * math.acos(max(min(self.q0, 1), -1))

    def getAxis(self):
        identity_thresh = 0.0001
        w, x, y, z = self.q0, self.q1, self.q2, self.q3
        Nq = numpy.linalg.norm(self.matrix)
        if not numpy.isfinite(Nq):
            return numpy.array([1.0, 0, 0])
        if Nq < identity_thresh ** 2:  # Results unreliable after normalization
            return numpy.array([1.0, 0, 0])
        if not numpy.isclose(Nq, 1):  # Normalize if not normalized
            s = math.sqrt(Nq)
            w, x, y, z = w / s, x / s, y / s, z / s
        len2 = x*x + y*y + z*z
        if len2 < identity_thresh**2:
            # if vec is nearly 0,0,0, this is an identity rotation
            return numpy.array([1.0, 0, 0])
        # Make sure w is not slightly above 1 or below -1
        theta = 2 * math.acos(max(min(w, 1), -1))
        return numpy.array([x, y, z]) / math.sqrt(len2)
