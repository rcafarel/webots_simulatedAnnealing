import random
import math

from src.matrix.DH import DH
from src.Configuration import Configuration

maxLength = 200.0
maxRadian = 2.0 * math.pi



def randomValue(multiplier):
    return random.uniform(0.0, 1.0) * multiplier


def randomAcceptance():
    rand = randomValue(1.0)
    return rand < Configuration.acceptanceLevel


def initialGuess(guessedPose):

    guessedPose.dh1 = DH(0, 0, 27.0, 0)
    guessedPose.dh2 = DH(0, 0, 44.0, math.pi/2.0)
    guessedPose.dh3 = DH(0, 0, 75.0, 0)
    guessedPose.dh4 = DH(0, math.atan2(91.0, -101.0), 137.0, 0)





def getStepLength(initialLength, temp):
    lengthChange = (randomValue(2.0) - 1.0) * maxLength / 2.0 * temp
    updatedLength = initialLength + lengthChange
    # return min(max(0, updatedLength), maxLength)
    return min(max(-1.0*maxLength, updatedLength), maxLength)

def getStepRadian(initialLength, temp):
    radianChange = (randomValue(2.0) - 1.0) * maxRadian / 2.0 * temp
    updatedRadian = initialLength + radianChange
    return min(max(-1.0 * math.pi, updatedRadian), math.pi)



stepCounter = 0
def incrementStepCounter():
    global stepCounter
    stepCounter += 1

def applyStep(guessedPose, currentTemperature):
    guessedPose.dh1.d = getStepLength(guessedPose.dh1.d, currentTemperature)
    guessedPose.dh1.theta = getStepRadian(guessedPose.dh1.theta, currentTemperature)
    guessedPose.dh1.a = getStepLength(guessedPose.dh1.a, currentTemperature)
    guessedPose.dh1.alpha = getStepRadian(guessedPose.dh1.alpha, currentTemperature)
    guessedPose.dh1.updateMatrix()

    guessedPose.dh2.d = getStepLength(guessedPose.dh2.d, currentTemperature)
    guessedPose.dh2.theta = getStepRadian(guessedPose.dh2.theta, currentTemperature)
    guessedPose.dh2.a = getStepLength(guessedPose.dh2.a, currentTemperature)
    guessedPose.dh2.alpha = getStepRadian(guessedPose.dh2.alpha, currentTemperature)
    guessedPose.dh2.updateMatrix()

    guessedPose.dh3.d = getStepLength(guessedPose.dh3.d, currentTemperature)
    guessedPose.dh3.theta = getStepRadian(guessedPose.dh3.theta, currentTemperature)
    guessedPose.dh3.a = getStepLength(guessedPose.dh3.a, currentTemperature)
    guessedPose.dh3.alpha = getStepRadian(guessedPose.dh3.alpha, currentTemperature)
    guessedPose.dh3.updateMatrix()

