import sys

number = str(sys.stdin.readline()).strip()
N = len(number)
count = 0 
resert = set()

def dfs(left, right, n, t):
    global count
    tmp_t = t

    if left > 0 :
        tmp_t = t
        tmp_t = tmp_t + (number[left-1: right+1],)
        dfs(left-1, right, n+1, tmp_t)

    if right < N-1 :
        tmp_t = t
        tmp_t = tmp_t + (number[left: right+2],)
        dfs(left, right+1, n+1, tmp_t)
    
    if(n == N-1):
        resert.add(tmp_t)
        return

for i in range(N):
    t = tuple(number[i],)
    dfs(i, i, 0, t)
print(len(resert))
