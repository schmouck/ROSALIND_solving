# Joël Simoneau
# Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)

import tools.files as tf

# Import file
filename = '5_FIB.txt'
file = os.path.join(relPath, 'inputData', filename)
data = [int(N) for N in tf.read_file(file).split()]

def fiboRabbit(n, k):
    rabbit = [1, 1]
    for i in range(n-2):
        rabbit.append(rabbit[i]*k + rabbit[i+1])
    return rabbit
    

print(fiboRabbit(data[0], data[1])[-1])