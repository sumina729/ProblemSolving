dp = [[[0 for _ in range(61)]for _ in range(61)]for _ in range(61)]

def dfs(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 0

    if not dp[a][b][c] == 0:
        return dp[a][b][c]
    
    dp[a][b][c] = 1 + min(dfs(max(a-1,0), max(b-3,0), max(c-9,0)), 
                          dfs(max(a-1,0), max(b-9,0), max(c-3,0)), 
                          dfs(max(a-3,0), max(b-1,0), max(c-9,0)), 
                          dfs(max(a-3,0), max(b-9,0), max(c-1,0)), 
                          dfs(max(a-9,0), max(b-1,0), max(c-3,0)), 
                          dfs(max(a-9,0), max(b-3,0), max(c-1,0)))
    return dp[a][b][c]
    
    
N = int(input())
n_list = list(map(int, input().split()))
n_list.append(0)
n_list.append(0)

print(dfs(n_list[0], n_list[1], n_list[2]))

        
