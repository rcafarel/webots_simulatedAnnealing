This algorithm takes as input arrays of pose data outputted by the webots_poseGatheringController.
The algorithm is designed to minimize the sum of the calculated end-effector positions based on forward kinematic equations compared to the estimated foot positions from the controller.
The output of this algorithm is the optimal DH parameters for the leg in two formats:
  1) parameters defined to be input into the WorldFileContent.py script used to generate a new webots world file.
  2) DHSegment objects to be input into the webots_walkingController PriorDHLegModels.py
