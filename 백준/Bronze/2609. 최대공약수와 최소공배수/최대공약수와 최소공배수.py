import sys
input = sys.stdin.readline

a, b = map(int, input().split())

#최대 공약수
def gcd(a, b):
    if b ==0:
        return a
    if a%b == 0:
        return b
    else :
        return gcd(b, a%b)

print(gcd(a, b))
print(int(a*b/gcd(a, b)))
