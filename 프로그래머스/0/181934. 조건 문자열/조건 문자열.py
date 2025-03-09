def solution(ineq, eq, n, m):
    if eq == '!' : eq = ''
    answer = int(bool(eval(f'{n}{ineq}{eq}{m}')))
    return answer