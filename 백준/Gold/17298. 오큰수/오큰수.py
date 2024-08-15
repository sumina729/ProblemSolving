import sys
input = sys.stdin.readline

N = int(input())
A_n = list(map(int, input().split()))

stack = []
resert = []
for i in range(N-1, -1, -1): 
    while True:
        if stack:
            if stack[-1] > A_n[i] :
                resert.append(stack[-1])
                stack.append(A_n[i])
                break
            else:
                stack.pop()
        else : 
            resert.append(-1)
            stack.append(A_n[i])
            break
      
print(*resert[::-1] )