def solution(num_list):
    even = sum(num_list[0::2])
    odd = sum(num_list[1::2])
    return max(even, odd)