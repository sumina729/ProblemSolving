import sys
import math
input = sys.stdin.readline



#소수판별
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:
            return False
    return True

N = int(input())
list_num = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if is_prime_number(list_num[i]) and not list_num[i] ==1:
        cnt+=1

print(cnt)
