def solution(s):
    answer = []
    s = s.split(" ")
    for i in s:
        l = ''
        for idx, j in enumerate(i):
            if idx%2 == 0:                
                l += j.upper()
            elif idx%2 == 1:
                l += j.lower()
        answer.append(l)   
            
            
    return " ".join(answer)