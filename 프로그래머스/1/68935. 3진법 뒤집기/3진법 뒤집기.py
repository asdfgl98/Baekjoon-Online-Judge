def solution(n):
    answer = 0
    num = n
    t = []
    while num > 0:
        t.append(num%3)
        num = num//3
    t.reverse()    
    for i in range(len(t)):
        answer += t[i]*(3**i)        
    
    return answer