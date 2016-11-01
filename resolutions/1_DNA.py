#Joël Simoneau
#Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)
    
import tools.files as tf
import tools.sequence as ts

# Import file
file = os.path.join(relPath, 'inputData', '1_DNA.txt')

# Create sequence object
sequence = ts.Sequence(tf.readFile(file))

# Count per nucleotide
listN = ['A', 'C', 'G', 'T']
for N in listN:
    print(sequence.countN(N))