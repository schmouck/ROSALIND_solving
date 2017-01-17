# Joël Simoneau
# Submission for ROSALIND

import tools.sequence as ts

def read_file(fname):
    with open(fname) as f:
        content = f.readlines()
    content = remove_break(content)
    if len(content) == 1:
        content = content[0]
    return content
    
def remove_break(content):
    for i in range(len(content)):
        if content[i][-1:] == '\n':
            content[i] = content[i][:-1]
    return content

def create_dictfasta(listfasta):
    dictfasta = {}
    currfasta = ""
    for line in listfasta:
        if line[0] == ">":
            currfasta = str(line)
            dictfasta[currfasta] = ""
        else:
            dictfasta[currfasta] += line
    return dictfasta

    
def read_fastafile(fname):
    listfasta = read_file(fname)
    dictfasta = create_dictfasta(listfasta)
    return [ts.Sequence(dictfasta[seq], fasta=seq[1:]) for seq in dictfasta]
