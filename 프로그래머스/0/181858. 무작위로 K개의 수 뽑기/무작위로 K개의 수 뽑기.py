def solution(arr, k):
    answer=[]
    [answer.append(i) for i in arr if not i in answer]
    if len(answer[:k]) != k:
        [answer.append(-1) for i in range(k-len(answer))]
        return answer
    else:
        return answer[:k]