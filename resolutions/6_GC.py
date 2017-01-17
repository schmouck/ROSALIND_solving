#Joël Simoneau
#Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)

import tools.files as tf

# Import file
filename = '6_GC.txt'
file = os.path.join(relPath, 'inputData', filename)
data = tf.read_fastafile(file)

# Sorting by GC content
data.sort(key = lambda seq: seq.gccontent)

print(data[-1].fasta)
print(data[-1].gccontent*100)