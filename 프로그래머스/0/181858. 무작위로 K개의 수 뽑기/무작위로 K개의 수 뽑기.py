def solution(arr, k):
    answer=[]
    [answer.append(i) for i in arr if not i in answer]
    return answer[:k] + [-1] * (k-len(answer))