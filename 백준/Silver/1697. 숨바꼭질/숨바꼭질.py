from collections import deque

N, K = map(int, input().split())
d_list = [-1 for _ in range(100001)]

def dfs(n):
    que = deque()
    que.append(n)
    d_list[n] = 0

    while que:
        n = que.popleft()

        if n == K:
            return d_list[n]

        t = [n+1, n-1, n*2]
        for i in range(3):
            if 0 <= t[i] <= 100000 and d_list[t[i]] == -1 :
                que.append(t[i])
                d_list[t[i]] = d_list[n]+1
        

print(dfs(N))