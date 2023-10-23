def solution(strings, n):
    answer = []
    for i in strings:
        strings.sort()
        strings.sort(key= lambda x: x[n])
    return strings