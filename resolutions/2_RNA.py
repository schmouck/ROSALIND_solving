#Joël Simoneau
#Submission for ROSALIND

import os, sys
relPath = os.path.abspath("..")
if relPath not in sys.path:
    sys.path.insert(0, relPath)
    
import tools.files as tf
import tools.sequence as ts    
    
# Import file
file = os.path.join(relPath, 'inputData', '2_RNA.txt')

# Create sequence object
sequence = ts.Sequence(tf.readFile(file))

sequence.DNA2RNA()
print(sequence.sequence)