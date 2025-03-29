def solution(rank, attendance):
    sortedrank = sorted([v for v, k in zip(rank, attendance) if k==True])
    answer = [rank.index(i) for i in sortedrank]
    return answer[0]*10000 + answer[1]*100 + answer[2]