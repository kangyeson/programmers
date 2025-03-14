def solution(arr, queries):
    for s, e, k in queries:
        l = [i for i in range(len(arr)) if s<=i<=e and i%k==0]
        arr = [arr[x]+1 if x in l else arr[x] for x in range(len(arr))]
    return arr