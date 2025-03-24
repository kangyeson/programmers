def solution(num_list):
    answer = 0
    for v in num_list:
        while v != 1:
            if v%2==0:
                v = int(v/2)
                answer+=1
            else:
                v = int((v-1)/2)
                answer+=1
    return answer