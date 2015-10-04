
import os
import numpy as np
import pickle


class ExportData:
    def get_plot(self, sub_no, cup_no, speed):
        return self

    def get_speed(self, sub_no, vcup_no, trj):
        return self


rootDir = '.'
raw_data = []
tree = {}
# Directory Traversal
for dirName, subdirList, fileList in os.walk(rootDir):
    # Iterate through file list and parse any file that ends with .csv
    for fname in fileList:
        if fname.endswith(".txt"):
            f = os.path.join(dirName, fname)

            subj_name = dirName[6:9]
            # Use numpy to create an arrays from the data
            time_array, distance_array = np.genfromtxt(f, skip_header=1, unpack=True)
            combined_array = [time_array, distance_array]

            file = open(f)
            line = file.readline()
            pathname = line.rsplit('/', 1)
            pathname[1] = pathname[1].strip()
            keys = pathname[1].split('_')
            keys.pop(0)
            if 'down' in keys:
                keys[0:2] = [''.join(keys[0:2])]
            keys[3] = keys[3][:2]

            if subj_name not in tree:
                tree[subj_name] = {}
            if keys[0] not in tree[subj_name]:
                tree[subj_name][keys[0]] = {}
            if keys[1] not in tree[subj_name][keys[0]]:
                tree[subj_name][keys[0]][keys[1]] = {}
            if keys[2] not in tree[subj_name][keys[0]][keys[1]]:
                tree[subj_name][keys[0]][keys[1]][keys[2]] = {}
            if keys[3] not in tree[subj_name][keys[0]][keys[1]][keys[2]]:
                tree[subj_name][keys[0]][keys[1]][keys[2]][keys[3]] = []

            tree[subj_name][keys[0]][keys[1]][keys[2]][keys[3]].append(combined_array)
            # Type of Trajectory is an unique identifier to place each data set into a dictionary
            file.close()

output = open('test.cpickle', "wb")
pickle.dump(tree, output, protocol=2)
output.close()
