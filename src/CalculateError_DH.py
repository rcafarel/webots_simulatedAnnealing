import math

import numpy

from src.matrix.Translation import Translation
from src.matrix.Quaternion import Quaternion
from src.matrix.RotationZ import RotationZ



def calculateError(guessed, given):
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
    m = numpy.matmul(m, guessed.dh1.matrix)

    rz1 = RotationZ(s1)
    m = numpy.matmul(m, rz1.matrix)

    m = numpy.matmul(m, guessed.dh2.matrix)

    rz2 = RotationZ(s2)
    m = numpy.matmul(m, rz2.matrix)

    m = numpy.matmul(m, guessed.dh3.matrix)

    rz3 = RotationZ(s3)
    m = numpy.matmul(m, rz3.matrix)

    m = numpy.matmul(m, guessed.dh4.matrix)

    eex = m[0, 3] - given.ee_x
    eey = m[1, 3] - given.ee_y
    eez = m[2, 3] - given.ee_z

    error = math.sqrt(eex*eex + eey*eey + eez*eez)
    return error
