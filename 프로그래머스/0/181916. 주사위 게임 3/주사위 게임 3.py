def solution(a, b, c, d):
    dice = [a,b,c,d]
    c = [dice.count(x) for x in dice] 
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*dice[c.index(3)]+ dice [c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(dice[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(dice) + min(dice)) * abs(max(dice) - min(dice))
    else:
        return min(dice)
