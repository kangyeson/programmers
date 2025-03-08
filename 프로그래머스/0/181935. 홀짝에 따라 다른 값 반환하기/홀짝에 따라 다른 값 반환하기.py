def solution(n):
    answer = 0
    if n%2 == 0 :
        i = 2
        while i <= n :
            answer += i**2
            i+=2
    else :
        i = 1
        while i <= n :
            answer += i
            i+=2
    return answer