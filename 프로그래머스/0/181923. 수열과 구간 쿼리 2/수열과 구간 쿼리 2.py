def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = ([arr[i] for i in range(len(arr)) if s<=i<=e and arr[i]>k])
        if not a:
            answer.append(-1)
        else:
            answer.append(min(a))
    return answer