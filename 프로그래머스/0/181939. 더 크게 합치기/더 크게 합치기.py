def solution(a, b):
    answer = lamda x : int(str(a)+str(b)) if int(str(a)+str(b)) >= int(str(b)+str(a)) else int(str(b)+str(a))
    return answer