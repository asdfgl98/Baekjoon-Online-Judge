def solution(s):
    cnt = 0
    change_cnt = 0
    while s != "1":
        change_cnt += s.count('0')
        cnt += 1
        s = s.replace('0', '')
        l = len(s)
        s = str(bin(l)[2:])
    
    return [cnt, change_cnt]