import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
 
for _ in range(N-1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

resert_n = 0
resert = 0


def dfs(n, sum):
    global resert
    global resert_n
    is_leaf = True
    for i, w in tree[n]:
        if visited[i] == -1:
            visited[i] = 1
            dfs(i, sum+w)
    
    if is_leaf : 
        if sum >= resert :
            resert = sum
            resert_n = n
    
    
visited = [-1] * (N+1)
visited[1] = 1
dfs(1, 0)
visited = [-1] * (N+1)
resert=0
visited[resert_n] = 1
dfs(resert_n, 0)
print(resert)   