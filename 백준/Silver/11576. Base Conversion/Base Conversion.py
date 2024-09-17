import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
m_list = list(map(int, input().split()))

#A -> 10 
ten_num = 0
up = 0
while m_list:
    ten_num = ten_num + (m_list[-1]*(A**up))
    m_list.pop()
    
    up+=1

#10>B
b_list = []
while ten_num:
    b_list.append(ten_num%B)
    ten_num=ten_num//B

print(*b_list[::-1])