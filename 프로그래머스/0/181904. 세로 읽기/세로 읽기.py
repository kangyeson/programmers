def solution(my_string, m, c):
    answer = [my_string[i*m+(c-1)] for i in range(int(len(my_string)/m))]
    return ''.join(answer)