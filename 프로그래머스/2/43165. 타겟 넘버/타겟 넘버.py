
answer = 0

def dfs(numbers, n, sum, target): #백트레킹
    global answer
    if n == len(numbers):
        # print(sum)
        if sum == target:
            answer+=1
        return
        
    dfs(numbers, n+1, sum+numbers[n], target)
    dfs(numbers, n+1, sum-numbers[n], target)


def solution(numbers, target): # 리스트, 수
    global answer
    answer = 0
    
    dfs(numbers, 0, 0, target)
    
    
    return answer