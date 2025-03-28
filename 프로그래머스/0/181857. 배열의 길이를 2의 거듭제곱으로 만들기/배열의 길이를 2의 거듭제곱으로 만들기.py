def solution(arr):
    answer = []
    i=1
    while i*2<=len(arr):
        i *= 2
    if i==len(arr): 
        return arr
    elif i<len(arr):
        return arr+[0]*((i*2)-len(arr))