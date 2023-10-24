def solution(N, stages):
    answer = []
    stages.sort()
    s = len(stages)
    fail = {}
    for i in range(1, N+1):
        if s != 0:
            fail[i] = (stages.count(i)/s)
            s -= stages.count(i)
        else:
            fail[i] = 0
        
    answer = sorted(fail, key=lambda x:fail[x], reverse=True)
  
    
    
    return answer