def readFile(fname):
    with open(fname) as f:
        content = f.readlines()
    content = removeBreak(content)
    if len(content) == 1:
        content = content[0]
    return content
    
def removeBreak(content):
    for i in range(len(content)):
        if content[i][-1:] == '\n':
            content[i] = content[i][:-1]
    return content