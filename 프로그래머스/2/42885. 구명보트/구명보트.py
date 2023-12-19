def solution(people, limit):
    answer = []
    people.sort()
    # 보트 수
    cnt = 0
    # 가장 가벼운사람과 무거운사람 인덱스
    a, b = 0, len(people)-1
    
    while a <= b:
        if people[a] + people[b] <= limit:
            cnt +=1
            a += 1
            b -= 1
        else:
            cnt += 1
            b -= 1

        
    
    
    return cnt