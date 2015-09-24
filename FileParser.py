
import os
import math
import numpy as np
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

            subj_name = dirName[6:9]

            # i = int(subj_name)
            # type_of_trajectory += values[i] * math.pow(2, 10)

            file = open(f)
            line = file.readline()
            pathname = line.rsplit('/', 1)
            type_of_trajectory = subj_name + pathname[1]
            # Use numpy to create an arrays from the data
            time_array, distance_array = np.genfromtxt(f, skip_header=1, unpack=True)
            combined_array = [time_array, distance_array]

            k = [type_of_trajectory, combined_array]
            raw_data.append(k)
            file.close()
            nparray = np.array(raw_data, dtype=object)
            np.save("test", nparray)

# Save File; File Parser Complete?
# Tree/Graph Class File
# Then a Main Class/Calls File Parser, Then opens file and organizes it to tree
# numpy Plots? Based on user input.


