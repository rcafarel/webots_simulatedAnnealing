from src.GuessedPoseParameters_DH import GuessedPoseParameters_DH
from src.Configuration import Configuration, nextTemp
from src.Guess_DH import initialGuess, applyStep, randomAcceptance


def solve(givenPoses):
    guessedPose = GuessedPoseParameters_DH()
    initialGuess(guessedPose)

    bestError = guessedPose.getError(givenPoses)
    overallBestError = bestError
    bestGuess = guessedPose.clone()
    overallBestGuess = guessedPose.clone()
    currentTemperature = Configuration.initialTemperature

    currentIteration = 0
    overallBestCounter = 0

    while currentIteration < Configuration.iterations and currentTemperature > 0.0:
        currentGuess = bestGuess.clone()
        applyStep(currentGuess, currentTemperature)
        currentError = currentGuess.getError(givenPoses)

        if (currentError < bestError or randomAcceptance()):
            bestError = currentError
            bestGuess = currentGuess
            if bestError < overallBestError:
                overallBestError = bestError
                overallBestGuess = currentGuess
                overallBestCounter = 0
            else:
                overallBestCounter += 1
                if overallBestCounter >= 50:
                    overallBestCounter = 0
                    bestError = overallBestError
                    bestGuess = overallBestGuess

        currentTemperature = nextTemp(currentTemperature)
        currentIteration += 1

    return overallBestError, overallBestGuess
