import sys
import math
input = sys.stdin.readline

array = [True] * 1000001
for i in range(2, int(math.sqrt(len(array)) + 1)):	# 2부터 x의 제곱근까지의 숫자
    if array[i] == False:
        continue

    j = 2
    while i * j < 1000001:
        array[i * j] = False
        j += 1

array[1] = False
array[2] = False

while True:
    num = int(input())
    if num == 0 : break
    
    is_good = False
    for i in range(3, num, 2):
        if array[i] and array[num-i]:
            print(f"{num} = {i} + {num-i} ")
            is_good = True
            break

    if not is_good:
        print("Goldbach's conjecture is wrong.")