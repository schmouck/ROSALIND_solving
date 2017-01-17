#Joël Simoneau
#Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)
    
import tools.files as tf
import tools.sequence as ts

# Import file
filename = '1_DNA.txt'
file = os.path.join(relPath, 'inputData', filename)

# Create sequence object
sequence = ts.Sequence(tf.read_file(file))

# Count per nucleotide
listn = ['A', 'C', 'G', 'T']
for n in listn:
    print(sequence.count_n(n))