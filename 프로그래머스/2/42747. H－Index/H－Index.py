def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for idx, i in enumerate(citations):
        h = n - idx
        if i >= h:
            return h
    return answer