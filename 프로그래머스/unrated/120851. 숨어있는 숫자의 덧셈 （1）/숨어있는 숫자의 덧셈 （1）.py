def solution(my_string):
    return sum(map(int, [i for i in my_string if i.isdigit()]))