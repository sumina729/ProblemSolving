import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
string = str(sys.stdin.readline()).strip()
i = 0
coount = 0
answer = 0

while i < M:
    if string[i:i+3] == 'IOI' :
        coount+=1
        if coount == N :
            answer +=1
            coount -=1
        i+=2
    else:
        coount = 0
        i+=1

print(answer)
   