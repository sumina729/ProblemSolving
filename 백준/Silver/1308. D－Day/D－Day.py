import sys
N = list(map(int, sys.stdin.readline().split()))
M = list(map(int, sys.stdin.readline().split()))
y, m, d = N[0], N[1], N[2]

dd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d_day = 0
is_long = False

while(True):
    
    if N[0] == y+1000 and  N[1] == m and  N[2] == d :      
        is_long =True
        break

    if N[0] == M[0] and  N[1] == M[1] and  N[2] == M[2] : break
    
    if N[0]%400 == 0 : 
        dd[1] = 29
    elif N[0]%100 == 0:
        dd[1] = 28
    elif N[0]%4 == 0:
        dd[1] = 29
    else : dd[1] = 28

    N[2] +=1
    if N[2] > dd[N[1]-1] :
        N[2] = 1
        N[1] +=1
    
    if N[1] > 12 :
        N[1] = 1
        N[0] +=1

    d_day+=1

if is_long : print('gg')
else : print('D-' + str(d_day))