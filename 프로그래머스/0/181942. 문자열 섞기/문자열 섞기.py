def solution(str1, str2):
    answer = ''
    while len(str1) + len(str2) > 0:
        if len(str1) >= 1:
            answer = answer + str1[0]
            str1 = str1[1:]
        if len(str2) >= 1:
            answer = answer + str2[0]
            str2 = str2[1:]
    return answer