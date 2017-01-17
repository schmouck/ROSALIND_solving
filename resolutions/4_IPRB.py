# Joël Simoneau
# Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)

import tools.files as tf

# Import file
filename = '4_IPRB.txt'
file = os.path.join(relPath, 'inputData', filename)
data = tf.read_file(file).split()

def mendel(k, m, n):
    up = k*(k-1) + 2*k*(m+n) + 3*m*(m-1)/4 + n*m
    down = (k+m+n)*(k+m+n-1)
    return up/down
    
    
print(mendel(int(data[0]), int(data[1]), int(data[2])))