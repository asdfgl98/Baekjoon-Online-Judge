def solution(n, m):
    answer = [0,0]
    
    result = []
    for i in range(1, n+1):
        if n%i == 0:
            result.append(i)
    
    for i in range(1, m+1):
        if m%i == 0:
            if i in result:
                answer[0] = i
    answer[1] = (n*m) //answer[0]
        
        
        
            
    
    return answer