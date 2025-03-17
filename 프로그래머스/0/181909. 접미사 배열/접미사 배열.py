def solution(my_string):
    answer = [my_string[-i:] for i in range(int(len(my_string)+1/2))]
    answer.sort()
    return answer