def solution(my_string, indices):
    my_string=[v for k,v in enumerate(my_string) if not k in indices]
    return ''.join(my_string)