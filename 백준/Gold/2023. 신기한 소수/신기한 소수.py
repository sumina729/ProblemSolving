import sys
import math

N = int(sys.stdin.readline())

def in_prime_number(n):
     # 2부터 x의 제곱근 까지
    for i in range(2, int(math.sqrt(n))+1) :
        if n%i == 0 : return False
    return True

def dfs(n, num):
    if(n == N): 
        print(num)
        return
    
    for i in range(1, 10):
        tmp = num*10+i
        if(not tmp ==1 and in_prime_number(tmp)) :
            dfs(n+1, tmp)

dfs(0, 0)
    
