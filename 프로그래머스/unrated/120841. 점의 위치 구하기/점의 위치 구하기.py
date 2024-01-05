def solution(dot):
    # x+ y+ : 1
    # x- y+ : 2
    # x- y- : 3
    # x+ y- : 4
    answer = 0
    
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] <0:
        return 3
    elif dot[0] > 0 and dot[1] < 0 :
        return 4
    return answer