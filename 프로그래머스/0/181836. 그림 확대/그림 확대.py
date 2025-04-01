def solution(picture, k):
    answer = []
    for i in picture:
        change=''
        for j in i:
            change += j*k
        re = k
        while re:
            answer.append(change)
            re-=1
    return answer