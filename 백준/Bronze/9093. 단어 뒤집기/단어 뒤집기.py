import sys
from collections import deque

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    s = list(sys.stdin.readline().split())
    
    for i in range(len(s)):
        stack = []
        tmp = str(s[i])
        for j in range(len(tmp)):
            stack.append(tmp[j])
        for j in range(len(tmp)):
            print(stack.pop(), end="")
        print(" ", end="")
    print()