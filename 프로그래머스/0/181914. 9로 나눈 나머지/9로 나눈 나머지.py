def solution(number):
    return sum([int(number[i]) for i in range(len(number))])%9