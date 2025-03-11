def solution(a, b, c):
    answer = a+b+c
    j = int(a==b)+int(a==c)+int(b==c)
    if j >= 1:
        answer *= ((a**2)+(b**2)+(c**2))
    if j == 3:
        answer *= ((a**3)+(b**3)+(c**3))
    return answer