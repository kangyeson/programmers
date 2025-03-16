def solution(my_string, queries):
    for a, b in queries:
        ChangeList = list(my_string[a:b+1])
        ChangeList.reverse()
        start = lambda a: my_string[0:a] if a >= 0 else ''
        end = lambda b: my_string[b+1:len(my_string)] if b+1<=len(my_string) else ''
        my_string = start(a) + ''.join(ChangeList) + end(b)
    return my_string