def solution(n):
    answer = set(x for x in range(2, n+1))
    for i in range(2,n+1):
        if i in answer:
            answer -= set(x for x in range(i*2, n+1, i))
            
    
        
    return len(answer)