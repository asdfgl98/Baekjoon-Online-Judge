def solution(n_str):
    answer = 0
    l = len(n_str)
    for idx,i in enumerate(n_str):
        n = 0
        if i == '1':
            n = 1
        elif i == '2':
            n = 2
        elif i == '3':
            n = 3
        elif i == '4':
            n = 4
        elif i == '5':
            n = 5
        elif i == '6':
            n = 6
        elif i == '7':
            n = 7
        elif i == '8':
            n = 8
        elif i == '9':
            n = 9

        answer += n * (10 ** (l-(idx+1)))
    return answer 