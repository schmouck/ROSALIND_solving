#Joël Simoneau
#Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)
    
import tools.files as tf
import tools.sequence as ts

# Import file
fileName = '3_REVC.txt'
file = os.path.join(relPath, 'inputData', fileName)

# Create sequence object
sequence = ts.Sequence(tf.readFile(file))

print(sequence.sequenceRevComp)