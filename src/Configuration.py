
LINEAR = 0
EXPONENTIAL = 1


class Configuration:
    iterations = 20000
    coolingRate = 0.999
    coolingMethod = EXPONENTIAL
    initialTemperature = 1.0
    acceptanceLevel = 0.05
    numberOfTrials = 10


def nextTemp(currentTemp):
    if Configuration.coolingMethod == LINEAR:
        return currentTemp - Configuration.coolingRate
    if Configuration.coolingMethod == EXPONENTIAL:
        return currentTemp * Configuration.coolingRate
    return 0
