def solution(str1, str2):
    answer = ''
    while len(str1)+len(str2) > 0:
        answer = answer+str1[0]+str2[0]
        str1.lstrip()
        str2.lstrip()
    return answer