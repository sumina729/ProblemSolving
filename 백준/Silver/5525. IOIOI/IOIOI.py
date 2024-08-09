import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
string = str(sys.stdin.readline()).strip()

P_N =[]
count = 0

for i in range(0, 2*N+1):
    if i%2 == 0 : P_N.append("I")
    else : P_N.append("O")

for i in range(0, M - (2*N)):
    tmp = string[i:i+(2*N+1)]
    if(tmp == ''.join(P_N)): count+=1

print(count)
    
