def solution(arr):
    try:
        indexs = [i for i in range(len(arr)) if arr[i]==2]
        return arr[min(indexs):max(indexs)+1]
    except:
        return [-1]