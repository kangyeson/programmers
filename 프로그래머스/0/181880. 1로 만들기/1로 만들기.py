def solution(num_list):
    answer = 0
    for v in num_list:
        while v != 1:
            v //= 2
            answer += 1
    return answer