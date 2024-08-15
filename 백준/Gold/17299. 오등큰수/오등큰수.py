import sys
input = sys.stdin.readline

N = int(input())
A_n = list(map(int, input().split()))
F = {}
for i in range(N):
    if A_n[i] in F.keys() :
        F[A_n[i]] = F.get(A_n[i])+1
    else : F[A_n[i]] =1
# print(F)

stack = []
resert = []
for i in range(N-1, -1, -1): 
    while True:
        if stack:
            if not stack[-1] == A_n[i] and F[stack[-1]] > F[A_n[i]] :
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
