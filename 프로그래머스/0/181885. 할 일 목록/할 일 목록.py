def solution(todo_list, finished):
    answer = [v for v,f in zip(todo_list, finished) if not f]
    return answer