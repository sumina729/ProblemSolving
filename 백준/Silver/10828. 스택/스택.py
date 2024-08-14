import sys
from collections import deque

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    tmp = list(sys.stdin.readline().split())
    
    if tmp[0] == 'push':
        stack.append(tmp[1])
    elif tmp[0] == 'pop':
        if stack : print(stack.pop())
        else :  print(-1)
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        if stack : print(0)
        else :  print(1)
    elif tmp[0] == 'top':
        if stack : print(stack[-1])
        else :  print(-1)