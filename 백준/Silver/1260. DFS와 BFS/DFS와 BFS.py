import sys

N, M, V = map(int, sys.stdin.readline().split())
lists = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] #양방향

#인접행렬
adj_matrix = [[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(M):
    adj_matrix[lists[i][0]][lists[i][1]] = 1
    adj_matrix[lists[i][1]][lists[i][0]] = 1
# print(*adj_matrix)

#인접리스트
adj_list = [[] for _ in range(N+1)]
for i in range(N+1):
    for j in range(M):
        if lists[j][0] == i: adj_list[i].append(lists[j][1])
        if lists[j][1] == i: adj_list[i].append(lists[j][0])
# print(*adj_list)

#1-1) DFS(재귀, 행렬) 
def DFS_recursion_matrix(v):
    is_visited[v] = True  
    print(v, end=" ")
    for i in range(1, N+1):
        if adj_matrix[v][i] == 1: 
            if not is_visited[i]:    
                DFS_recursion_matrix(i)
        

#1-2) DFS(재귀, 리스트)
def DFS_recursion_list(v):
    is_visited[v] = True
    print(v, end=" ")
    for i in range(1, N+1):
        if i in adj_list[v]: 
            if not is_visited[i]:    
                DFS_recursion_matrix(i)

#1-3) DFS(스택, 행렬)
def DFS_stack_matrix(v):
    stack = []
    stack.append(v)

    while len(stack) != 0 :
        tmp = stack.pop()
        if not is_visited[tmp]:
            print(tmp, end=" ")
            is_visited[tmp] = True
            for i in range(N, 0, -1):
                if adj_matrix[tmp][i] == 1 : stack.append(i)
     

#1-4) DFS(스택, 리스트)
def DFS_stack_list(v):
    stack = []
    stack.append(v)

    while len(stack) != 0 :
        tmp = stack.pop()
        if not is_visited[tmp]:
            print(tmp, end=" ")
            is_visited[tmp] = True
            for i in range(N, 0, -1):
                if i in adj_list[tmp] : stack.append(i)

from collections import deque

#2-1) BFS(큐, 행렬)
def BFS_queue_matrix(v):
    queue = deque()
    queue.append(v)

    while len(queue) != 0:
        tmp = queue.popleft()
        if not is_visited[tmp]:
            print(tmp, end=" ")
            is_visited[tmp] = True

            for i in range(1, N+1): 
                if adj_matrix[tmp][i] == 1: queue.append(i)


#2-2) BFS(큐, 리스트)
def BFS_queue_list(v):
    queue = deque()
    queue.append(v)

    while len(queue) != 0:
        tmp = queue.popleft()
        if not is_visited[tmp]:
            print(tmp, end=" ")
            is_visited[tmp] = True

            for i in range(1, N+1): 
                if i in adj_list[tmp]: queue.append(i)

is_visited = [False]*(N+1)
# DFS_recursion_matrix(V)
# DFS_recursion_list(V)
# DFS_stack_matrix(V)
DFS_stack_list(V)

print()

is_visited = [False]*(N+1)
# BFS_queue_list(V)
BFS_queue_matrix(V)