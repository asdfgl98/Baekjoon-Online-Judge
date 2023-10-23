def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        n = 0
        for i in p:
            try:
                n += yearning[name.index(i)]
            except:
                continue
        answer.append(n)
    return answer