#Joël Simoneau
#Submission for ROSALIND
from collections import Counter

class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def countN(self, N):
        # Return the number of N appareance
        c = Counter(self.sequence)
        return c[N]
        
    def DNA2RNA(self):
        self.sequence = ''.join(['U' if N == 'T' else N for N in self.sequence])