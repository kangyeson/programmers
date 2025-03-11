def solution(num_list):
    return int(eval('*'.join([str(n) for n in num_list])) < (sum(num_list)**2))