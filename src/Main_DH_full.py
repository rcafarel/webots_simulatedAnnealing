import time

import numpy

from data.Webots_data import s1, s2, s3, H, q0, q1, q2, q3, x, y, z, x_actual, y_actual, z_actual
from src.matrix.RotationZ import RotationZ
from src import SimulatedAnnealing_DH
from src.GuessedPoseParameters_DH import GuessedPoseParameters_DH
from src.GivenPoseParameters_DH import GivenPoseParameters
from src.matrix.Quaternion import Quaternion
from src.Configuration import Configuration

import math
import transformations

print("Start Time:", time.strftime("%H:%M:%S", time.localtime()))

givenPoses = []


def initializePoseParameters():
    for index in range(len(H)):
        givenPose = GivenPoseParameters()
        givenPose.hip_connect_h = H[index]
        givenPose.s1 = s1[index]
        givenPose.s2 = s2[index]
        givenPose.s3 = s3[index]

        givenPose.hip_O_q0 = q0[index]
        givenPose.hip_O_q1 = q1[index]
        givenPose.hip_O_q2 = q2[index]
        givenPose.hip_O_q3 = q3[index]

        givenPose.ee_x = x_actual[index]
        givenPose.ee_y = y_actual[index]
        givenPose.ee_z = z_actual[index]

        q = Quaternion([givenPose.hip_O_q0, givenPose.hip_O_q1, givenPose.hip_O_q2, givenPose.hip_O_q3])
        m = numpy.matmul(q.matrix, RotationZ(math.pi / 2.0).matrix)
        q = transformations.quaternion_from_matrix(m)
        givenPose.hip_O_q0 = q[0]
        givenPose.hip_O_q1 = q[1]
        givenPose.hip_O_q2 = q[2]
        givenPose.hip_O_q3 = q[3]

        if givenPose.ee_z < 5 and givenPose.ee_z > 3:
            givenPoses.append(givenPose)


initializePoseParameters()

bestError = 99999.0
bestGuess = GuessedPoseParameters_DH()
errors = []
guesses = []

for trial in range(Configuration.numberOfTrials):
    currentError, currentGuess = SimulatedAnnealing_DH.solve(givenPoses)
    print(str(trial) + ": " + str(currentError))

    if currentError < bestError:
        bestError = currentError
        bestGuess = currentGuess

    errors.append(currentError)
    guesses.append(currentGuess)


print(bestError)
bestGuess.dh1.printString("1")
bestGuess.dh2.printString("2")
bestGuess.dh3.printString("3")
bestGuess.dh4.printString("4")

bestGuess.dh1.printDHLink()
bestGuess.dh2.printDHLink()
bestGuess.dh3.printDHLink()
bestGuess.dh4.printDHLink()



print("End Time:", time.strftime("%H:%M:%S", time.localtime()))
