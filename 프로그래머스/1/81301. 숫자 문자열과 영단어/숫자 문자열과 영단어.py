def solution(s):
    answer = 0
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx,i in enumerate(num):
        s = s.replace(i, str(idx))
        
    
    answer = s

    return int(answer)