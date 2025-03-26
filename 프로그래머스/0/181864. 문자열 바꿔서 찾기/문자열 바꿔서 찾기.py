def solution(myString, pat):
    myString = myString.translate(myString.maketrans("AB", "BA"))
    return int(pat in myString)