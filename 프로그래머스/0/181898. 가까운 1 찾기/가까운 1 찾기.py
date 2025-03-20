def solution(arr, idx):
    if 1 not in arr[idx:]:
        return -1
    else:
        return arr.index(1, idx)