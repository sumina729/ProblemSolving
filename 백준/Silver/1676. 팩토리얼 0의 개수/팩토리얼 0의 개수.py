import sys
input = sys.stdin.readline

n = int(input())
num = 1

for i in range(n, 0, -1):
    num*=i

count = 0
while True:
    if num%10 == 0:
        count +=1
        num = num//10
    else:
        break

print(count)