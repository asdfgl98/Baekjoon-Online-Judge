def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        n = s[:i].rfind(s[i])
        if n == -1:
            answer.append(n)
        else:            
            answer.append(i-n)
        
        
        
    return answer