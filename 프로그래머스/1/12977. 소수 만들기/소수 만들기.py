def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                n = nums[i]+nums[j]+nums[k]
                c = 0
                for q in range(1,n+1):
                    if n%q == 0:
                        c += 1
                if c == 2:
                    answer +=1
        

    return answer