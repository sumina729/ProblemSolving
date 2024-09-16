import sys
input = sys.stdin.readline

def gcd(a, b):
    if b ==0:
        return a
    if a%b == 0:
        return b
    else :
        return gcd(b, a%b)

N, S = map(int, input().split())
N_num = list(map(int, input().split()))


gcd_num = N_num[0]-S
for i in range(N):
    gcd_num = gcd(gcd_num, N_num[i]-S)


print(abs(gcd_num))