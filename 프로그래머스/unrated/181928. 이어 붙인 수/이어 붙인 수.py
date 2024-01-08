def solution(num_list):
    a = ''
    b = ''
    for i in num_list:
        if i % 2 == 0:
            b += str(i)
        else:
            a +=  str(i)
    
    return int(a) + int(b)