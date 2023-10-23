def solution(nums):
    answer = 0
    r = len(nums)//2
    p = list(set(nums))
    if len(p) > r:
        answer = r
    elif len(p) < r:
        answer = len(p)
    else:
        answer = r
    return answer