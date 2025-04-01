def solution(n):
    answer = []
    for i in range(n):
        newlist = []
        for j in range(n):
            if i==j:
                newlist.append(1)
            else:
                newlist.append(0)
        answer.append(newlist)
    return answer