def solution(nums):
    answer = 0
    
    N = len(nums)
    print(N)
    
    nums_s = set(nums)
    
    
    print(len(nums_s))
    
    if N//2 < len(nums_s):
        answer = N//2
    else:
        answer = len(nums_s)
    return answer