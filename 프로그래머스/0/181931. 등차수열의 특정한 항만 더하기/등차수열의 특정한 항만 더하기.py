def solution(a, d, included):
    answer = 0
    ap = a
    while len(included) > 0:
        if included[0]:
            answer += ap
            ap += d
        else :
            ap += d
        del included[0]
    return answer