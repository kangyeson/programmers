def solution(myString, pat):
    fIndex=0
    while myString[fIndex:].find(pat) != -1:
        fIndex+=1
    return myString[:fIndex+len(pat)-1]