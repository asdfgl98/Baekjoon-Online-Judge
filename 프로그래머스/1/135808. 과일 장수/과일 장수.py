def solution(k, m, score):
    answer = 0
    score.sort()
    score.reverse()
    r = len(score)//m
    for i in range(r):
        answer += min(score[i*m:(i*m)+m]) * m
    return answer