# 최대 공약수
def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

# 최소 공배수
def lcm(x,y):
    return x * y // gcd(x,y)


def solution(arr):
    n = arr[0]
    for i in arr[1:]:
        n = lcm(n,i) 
    
    return n