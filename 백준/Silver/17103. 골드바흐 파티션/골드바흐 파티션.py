import sys
import math
input = sys.stdin.readline

array = [True] * 1000001
array[1] = True
array[2] = True
for i in range(2, int(math.sqrt(len(array)) + 1)):	# 2부터 x의 제곱근까지의 숫자
    if array[i] == False:
        continue

    j = 2
    while i * j < 1000001:
        array[i * j] = False
        j += 1



N = int(input())
for _ in range(N):
    num = int(input())
    
    count = 0
    if num == 4:
        count = 1
    for i in range(3, num, 2):
        if array[i] and array[num-i]:
            if i > num-i :
                break
            count +=1
    
    print(count)