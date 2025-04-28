answer = 0
def dfs(numbers, n, sum, target): 
    global answer
    if n == len(numbers):
        if sum == target:
            answer+=1
        return
        
    dfs(numbers, n+1, sum+numbers[n], target)
    dfs(numbers, n+1, sum-numbers[n], target)


def solution(numbers, target): 
    global answer
    answer = 0
    
    dfs(numbers, 0, 0, target)
    
    return answer