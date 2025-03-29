def solution(strArr):
    counter = {}
    for value in strArr:
        try:
            counter[len(value)] += 1
        except:
            counter[len(value)]=1
    return max(counter.values())