def solution(k, score):
    answer = []
    q = []
    for i in score:
        if len(q) < k:
            q.append(i)
            q.sort()
        else:
            if q[0] < i:
                del q[0]
                q.append(i)
                q.sort()
        answer.append(min(q))
    
    
    return answer