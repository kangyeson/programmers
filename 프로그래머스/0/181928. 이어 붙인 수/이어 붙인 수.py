def solution(num_list):
    odd = [str(x) for x in num_list if x%2==1 ]
    even = [str(x) for x in num_list if x%2==0 ]
    return int(''.join(odd))+int(''.join(even))