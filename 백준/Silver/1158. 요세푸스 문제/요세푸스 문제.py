import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
for i in range(1, N+1) :
    queue.append(i)

n = 1
lists = []
while queue:
    if n == K:
        lists.append(str(queue.popleft()))
        n = 1
    else :
        queue.append(queue.popleft())
        n+=1

print("<", end="")
lists = ', '.join(lists)
print(lists, end="")
print(">", end="")
