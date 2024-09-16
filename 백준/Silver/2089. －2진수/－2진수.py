import sys
input = sys.stdin.readline

num = int(input())

resert =""


if num==0:
    print(0)
    exit
while num!=0:
    if num%(-2)!=0:
        resert +='1'
        num=num//(-2)+1
    else:
        resert +='0'
        num=num//(-2)

print(resert[::-1])