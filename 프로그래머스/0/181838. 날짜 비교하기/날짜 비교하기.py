def solution(date1, date2):
    answer = 0
    return int(int(''.join(map(str, date1))) < int(''.join(map(str, date2))))