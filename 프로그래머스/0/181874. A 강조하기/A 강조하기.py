def solution(myString):
    myString = myString.lower()
    transA = str.maketrans('a', 'A')
    myString = myString.translate(transA)
    return myString