def solution(arr):
    answer = []
    
    m = min(arr)
    arr.remove(m)
    
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr
    
    return answer