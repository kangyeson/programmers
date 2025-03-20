def solution(my_string):
    my_ORDList = [ord(my_string[i]) for i in range(len(my_string))]
    answer = [my_ORDList.count(i) for i in list(range(ord('A'), ord('Z')+1))+list(range(ord('a'), ord('z')+1))]
    
    return answer