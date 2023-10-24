def solution(number, limit, power):
    answer = 0
    result = []
    for i in range(1,number+1):
        c = 0
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                c += 2
        if i **0.5 %1 == 0:
            c -= 1
        
        if c <= limit:
            answer += c
        else:
            answer += power
    
 
    return answer