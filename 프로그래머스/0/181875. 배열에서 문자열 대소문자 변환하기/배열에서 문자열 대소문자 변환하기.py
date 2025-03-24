def solution(strArr):
    for i, v in enumerate(strArr):
        if i%2==1:
            strArr[i] = v.upper()
        else:
            strArr[i] = v.lower()
    return strArr