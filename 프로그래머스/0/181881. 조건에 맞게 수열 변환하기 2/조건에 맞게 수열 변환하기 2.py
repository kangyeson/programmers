def solution(arr):
    answer = 0
    newValue = []
    while 1:
        newValue = arr.copy()
        for i, value in enumerate(arr):
            if value>=50 and value%2==0:
                arr[i] = (int(value/2))
            elif value<50 and value%2==1:
                arr[i] = ((value*2)+1)
                
        if newValue == arr:
            return answer
        else:
            answer += 1
        