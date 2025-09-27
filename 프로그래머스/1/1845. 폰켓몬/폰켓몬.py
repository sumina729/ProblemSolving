def solution(nums):
    answer = 0
    
    l1 = len(nums)
    l2 = len(set(nums))
    
    if l1//2 < l2:
        answer = l1//2
    else:
        answer = l2
    return answer