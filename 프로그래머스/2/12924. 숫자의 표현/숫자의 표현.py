def solution(n):
    answer = 0

    for i in range(1,n+1):
        cnt = i
        if i == n:
            answer += 1
            return answer
        for j in range(i+1, n+1):
            cnt += j
            if cnt == n:
                answer += 1
                break
            elif cnt > n:
                break
            
    
    return answer