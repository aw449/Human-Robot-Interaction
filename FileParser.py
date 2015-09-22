
import os
import math
import numpy as np


class Classifier:

    def __init__(self, string):
        self._string = string
        self._parameters = []

    def analyze(self):
        self._parameters = self._string.split('_')
        trj = 0
        if len(self._parameters) == 6:
            i = 1
            trj += 256
        else:
            i = 0
            if self._parameters[1] == "straight":
                trj += 128
            if self._parameters[1] == "short":
                trj += 384
            if self._parameters[1] == "curve":
                trj += 512
        hand = self._parameters[2+i]
        cup = self._parameters[3+i]
        speed = self._parameters[4+i]
        if hand == "right":
            trj += 64
        m = 0
        for x in range(2, 12):
            if cup == x:
                trj += math.pow(2, 2+m)
            m += 1
        if speed == "10.0.ts":
            trj += 1
        if speed == "5.0.ts":
            trj += 2
        return trj


rootDir = '.'
values = list(range(1, 17))
raw_data = []
# Directory Traversal
for dirName, subdirList, fileList in os.walk(rootDir):
    # Iterate through file list and parse any file that ends with .csv
    for fname in fileList:
        if fname.endswith(".csv"):
            f = os.path.join(dirName, fname)

            # Type of Trajectory is an unique identifier to place each data set into a dictionary
            type_of_trajectory = 0
            subj_name = dirName[4:6]

            i = int(subj_name)
            type_of_trajectory += values[i] * math.pow(2, 10)

            file = open(f)
            line = file.readline()
            pathname = line.rsplit('/', 1)
            a = Classifier(pathname)
            type_of_trajectory += a.analyze()

            # Use numpy to create an arrays from the data
            time_array, distance_array = np.genfromtxt(f, skip_header=1, unpack=True)
            k = [type_of_trajectory, time_array, distance_array]
            raw_data.append(k)
            file.close()


# Save File; File Parser Complete?
# Tree/Graph Class File
# Then a Main Class/Calls File Parser, Then opens file and organizes it to tree
# numpy Plots? Based on user input.


