def solution(myStr):
    a = str.maketrans("abc", "   ")
    myStr = myStr.translate(a).strip()
    if myStr == "":
        return ["EMPTY"]
    else:
        return myStr.split()