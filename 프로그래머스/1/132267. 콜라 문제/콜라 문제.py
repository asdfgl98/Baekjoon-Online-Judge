def solution(a, b, n):
    answer = 0
    while n >= a:
        if n < 2:
            break
        answer += (n//a)*b
        n = (n%a) + (n//a)*b
    return answer