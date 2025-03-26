def solution(my_string):
    my_string = my_string.strip()
    my_string = my_string.split(' ')
    return [i for i in my_string if i!=""]