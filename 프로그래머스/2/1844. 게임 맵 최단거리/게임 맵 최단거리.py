from collections import deque

def bfs(x, y, maps):
    global n, m
    
    visited = [ [ -1 for _ in range(m) ] for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    
    que = deque()
    que.append((x, y))
    visited[y][x] = 1
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if -1 < nx < m and -1 < ny < n and visited[ny][nx] == -1 and maps[ny][nx] == 1:
                
                visited[ny][nx] = visited[y][x] + 1
                que.append((nx, ny))
                
    return visited[n-1][m-1]
                
        
    
    
n, m = 0, 0

def solution(maps):
    answer = 0
    
    global n, m
    
    n, m = len(maps), len(maps[0])
    answer = bfs(0, 0, maps)
    
    return answer