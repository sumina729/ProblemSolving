N = int(input())
row = [-1 for i in range(N)]
count = 0



def is_set(row_n, col_n):
    for i in range(row_n):
        if row[i] == col_n : 
            return False
        if row[i] == col_n-(row_n-i) : 
            return False
        if row[i] == col_n+(row_n-i) : 
            return False
    # print(row)
    #if(row_n == 2): print(row[i], col_n-(row_n-i))
    return True


def set_Q(row_n):
    global count

    if(row_n == N):
        count+=1
        return
    
    for col_n in range(0, N):
        #print(row_n, col_n)
        if(is_set(row_n, col_n)):
            row[row_n] = col_n
            
            set_Q(row_n+1)
            


set_Q(0)
print(count)

