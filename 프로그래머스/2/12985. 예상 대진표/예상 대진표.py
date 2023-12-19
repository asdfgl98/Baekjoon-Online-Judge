def solution(n,a,b):
    # n = 참가자수
    # a = 참가자 A 번호
    # b = 경쟁자 번호
    answer = [i for i in range(1,n+1)]
    new = []
    round = 0
    while True:
        round += 1
        new = []
        for i in range(0, len(answer),2):
            if (answer[i] == a or answer[i] == b) and (answer[i+1] == a or answer[i+1] == b):
                return round
            elif answer[i] == a or answer[i] == b:
                new.append(answer[i])
            elif answer[i+1] == a or answer[i+1] == b:
                new.append(answer[i+1])
            else:
                new.append(answer[i])
            
        answer = new
                   

    return answer