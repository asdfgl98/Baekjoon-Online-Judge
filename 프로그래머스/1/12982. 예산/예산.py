def solution(d, budget):
    answer = 0
    d.sort()
    
    for idx, i in enumerate(d):
        budget -= i
        
        if budget < 0:
            return idx
        
        

    return len(d)