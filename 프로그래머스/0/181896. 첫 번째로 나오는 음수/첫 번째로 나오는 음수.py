def solution(num_list):
    try:
        return [num_list.index(i) for i in num_list if i<0][0]
    except:
        return -1