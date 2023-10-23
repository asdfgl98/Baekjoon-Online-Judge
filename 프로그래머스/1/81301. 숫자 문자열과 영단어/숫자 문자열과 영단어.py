def solution(s):
    answer = 0
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx,i in enumerate(num):
        if s.find(i) != -1:
            s = s.replace(s[s.find(i):s.find(i)+len(i)], str(idx))
    
    answer = s

    return int(answer)