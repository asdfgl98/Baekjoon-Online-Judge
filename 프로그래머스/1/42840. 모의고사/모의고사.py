def solution(answers):
    answer = []
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0,0,0]
    for idx,i in enumerate(answers):
        if n1[idx % len(n1)] == i:
            result[0] +=1
        if n2[idx % len(n2)] == i:
            result[1] += 1
        if n3[idx % len(n3)] == i:
            result[2] += 1        
            
    
    for idx, i in enumerate(result):
        if i == max(result):
            answer.append(idx+1)
            
    return answer