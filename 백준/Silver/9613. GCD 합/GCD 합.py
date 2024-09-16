import sys
input = sys.stdin.readline


#최대 공약수
def gcd(a, b):
    if b ==0:
        return a
    if a%b == 0:
        return b
    else :
        return gcd(b, a%b)


t = int(input())

for i in range(t):
    num = list(map(int, input().split()))

    resert = 0
    for j1 in range(1, num[0]+1):
        for j2 in range(j1+1, num[0]+1):
            resert+=gcd(num[j1], num[j2])

    print(resert)