import sys
import math
input = sys.stdin.readline

a, b= map(int, input().split())
array = [True for _ in range(b+1)]

for i in range(1, b+1):	# 2부터 x의 제곱근까지의 숫자
    if i ==1 :
        array[i] = False

    if array[i] == False:
        continue
    
    j = 2
    while i * j <= b:
        array[i * j] = False
        j += 1
    

for i  in range(a, b+1): 
    if array[i] :
        print(i)