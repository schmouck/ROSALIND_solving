# Joël Simoneau
# Submission for ROSALIND
from collections import Counter

class Sequence:
    def __init__(self, sequence, fasta = ''):
        self.sequence = sequence
        self.fasta = fasta
        self.dictdna = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

        self.sequence_revcomp = self.revcomp()
        self.gccontent = self.count_gc()
    
    def count_n(self, n):
        # Return the number of N appareance
        c = Counter(self.sequence)
        return c[n]
        
    def dna2rna(self):
        self.sequence = ''.join(['U' if N == 'T' else N for N in self.sequence])

    def rna2prot(self):
        # TODO
        
    def revcomp(self):
        return ''.join([self.dictdna[N] for N in self.sequence[::-1]])
        
    def count_gc(self):
        return sum([1 if N in 'GC' else 0 for N in self.sequence])/len(self.sequence)
