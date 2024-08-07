N, M = map(int, input().split())
sequence = [0 for i in range(M)]

def backtracking(m):
    if m == M:
        for i in range(M):
            print(sequence[i], end=" ")
        print()
        return
    
    for i in range(1, N+1):
        is_tmp = True
        for j in range(m):
            if(i < sequence[j]): is_tmp = False
        if(is_tmp) :
            sequence[m] = i
            backtracking(m+1)
        
                 
backtracking(0)  
