
import os
import numpy as np

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    file = open(f)
    line = file.readline()
    # Read in type of trajectory and classify it
    file.close()
