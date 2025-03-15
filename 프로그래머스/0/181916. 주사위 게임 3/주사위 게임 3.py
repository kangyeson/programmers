def solution(a, b, c, d):
    answer = 1111*a
    dice = [a, b, c, d]
    equlnum = {}
    for i in dice:
        if i in equlnum:
            equlnum[i]+=1
        else:
            equlnum[i]=1
    
    for key, value in equlnum.items():
        diffnum = [k for k, v in equlnum.items() if key != k]
        if value == 3:
            answer = (10 * key + diffnum[0])**2
            break
            
        elif value == 2:
            if len(diffnum)==1:
                answer = (key + diffnum[0]) * abs(key-diffnum[0])
                break
            else:
                answer = diffnum[0]*diffnum[1]
                break
            
        elif value == 1:
            answer = min(dice)
        
    return answer