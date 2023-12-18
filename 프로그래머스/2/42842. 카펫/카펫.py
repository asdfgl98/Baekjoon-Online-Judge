def solution(brown, yellow):
    answer = []

    all = int(brown) + int(yellow)
    for i in range(3, all+1):
        if all % i == 0:
            x = all/i
            if (x-2) * (i-2) == yellow:
                return [x,i]

    

    
    
        
    return answer