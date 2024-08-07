N, M = map(int, input().split())
number = [0 for i in range(N)]
sequence = [0 for i in range(M)]

def backtracking(m):
    if m == M:
        for i in range(M):
            print(sequence[i], end=" ")
        print()
        return
    
    for i in range(0, N):
        is_tmp = True
        for j in range(m):
            if(number[i] == sequence[j]): is_tmp = False
        if(is_tmp) :
            sequence[m] = number[i]
            backtracking(m+1)
        
tmp_num = input().split()
for i in range(0, N):
   number[i] = int(tmp_num[i])
number.sort()            
backtracking(0)  
