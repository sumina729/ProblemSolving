import sys
from collections import deque

N = int(sys.stdin.readline())
list = deque()
throw = []
is_throw = True

for i in range(N):
    list.append(i+1)

while(True):
    if(len(list)==0): break

    if is_throw :
        throw.append(list.popleft())
        is_throw = False
    else :
        list.append(list.popleft())
        is_throw = True

print(*throw)