def solution(babbling):
    answer = 0
    b = ['aya', 'ye', 'woo', 'ma']
            
    for idx in range(len(babbling)):
        
        for j in b:
            if j in babbling[idx] and (j*2 not in babbling[idx]):
                babbling[idx] = babbling[idx].replace(j, '*')
            
        if all(k == '*' for k in babbling[idx]):
             answer += 1
        

    
    return answer