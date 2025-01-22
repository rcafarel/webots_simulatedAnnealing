import math

from src.matrix.DH import DH
from src.matrix.RotationZ import RotationZ
from src.matrix.Translation import Translation
from src.matrix.Quaternion import Quaternion
import numpy

from src import CalculateError_DH


class GuessedPoseParameters_DH:

    def __init__(self):

        self.dh1 = DH(0, 0, 0, 0)
        self.dh2 = DH(0, 0, 0, 0)
        self.dh3 = DH(0, 0, 0, 0)
        self.dh4 = DH(0, 0, 0, 0)

        self.error = 0

    def getError(self, givenPoses):
        self.error = 0
        self.calculateLL(givenPoses[0])

        for givenPose in givenPoses:
            self.error += CalculateError_DH.calculateError(self, givenPose)

        return self.error

    def calculateLL(self, given):
        hip_connect_h = given.hip_connect_h
        hip_O_q0 = given.hip_O_q0
        hip_O_q1 = given.hip_O_q1
        hip_O_q2 = given.hip_O_q2
        hip_O_q3 = given.hip_O_q3
        s1 = given.s1
        s2 = given.s2
        s3 = given.s3

        h = Translation([0, 0, hip_connect_h])
        hq = Quaternion([hip_O_q0, hip_O_q1, hip_O_q2, hip_O_q3])

        m = numpy.matmul(h.matrix, hq.matrix)
        m = numpy.matmul(m, self.dh1.matrix)

        rz1 = RotationZ(s1)
        m = numpy.matmul(m, rz1.matrix)

        m = numpy.matmul(m, self.dh2.matrix)

        rz2 = RotationZ(s2)
        m = numpy.matmul(m, rz2.matrix)

        m = numpy.matmul(m, self.dh3.matrix)

        rz3 = RotationZ(s3)
        m = numpy.matmul(m, rz3.matrix)


        # ee = Translation([given.ee_x, given.ee_y, given.ee_z])
        T = numpy.matmul(numpy.linalg.inv(m), numpy.transpose([given.ee_x, given.ee_y, given.ee_z, 1]))

        self.dh4.d = T[2]
        self.dh4.theta = math.atan2(T[1], T[0])
        self.dh4.a = T[0] / math.cos(self.dh4.theta)
        self.dh4.updateMatrix()

    def clone(self):
        clone = GuessedPoseParameters_DH()
        clone.dh1 = self.dh1.clone()
        clone.dh2 = self.dh2.clone()
        clone.dh3 = self.dh3.clone()
        clone.dh4 = self.dh4.clone()
        clone.error = self.error
        return clone
