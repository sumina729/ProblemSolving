import sys
N, M = map(int, sys.stdin.readline().split())
lists = list(map(int, sys.stdin.readline().split()))
locate_1 = []
n = 0
nn = 1
s, e = 0, 0
min_n = N+1

while(True):
    if s >= N or lists[s] == 1:
        e = s+1
        locate_1.append(s)
        break
    s+=1    

while(e<N):
    if(lists[e] == 1):
        if(M == 1) : min_n =1
        n+=1
        locate_1.append(e)

        if(n==M-1): 
            min_n = min(e-s+1, min_n)
            n-=1
            s=locate_1[nn]
            nn+=1
            #del locate_1[0]
    e+=1

if(min_n > N) : print(-1)
else : print(min_n)
