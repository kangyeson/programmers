def solution(arr):
    stk = [arr[0]]
    i=1
    while i<len(arr):
        if not stk:
            stk.append(arr[i])
            i+=1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            del stk[-1]
    return stk