def solution(s):
    answer = 0
    # s = list(s)
    origin_s = s
    result = []
    x = s[0]
    same = 0
    anther = 0
    idx = 0
    
    for ids,i in enumerate(s):
        print(i, x)
        if i == x:
            same += 1
        else:
            anther += 1 
        if same != 0 and same == anther:
            result.append(s[:idx+1])
            s = s[idx+1:]

            if len(s) == 0:
                break
            else:
                x = s[0]
                same = 0
                anther = 0
                idx = 0
                continue
        
        elif ids+1 == len(origin_s) and same != anther:
            result.append(i)            
            
        idx +=1
        
    return len(result)