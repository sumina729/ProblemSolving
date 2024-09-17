import sys
input = sys.stdin.readline

N, B = map(int, input().split())

lsets = ['0, ''1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']

resert =""

if N==0:
    print(0)
    exit

while N!=0:
    if N%B < 10:
        resert+=str(N%B)
    else: 
        resert+=chr(65+(N%B)-10)
    
    N=N//B

print(resert[::-1])