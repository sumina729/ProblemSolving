N = int(input())
number = list(map(int, input().split())) #N
op = list(map(int, input().split())) #4
min_num = 1000000000
max_num = -1000000000

def calculate(n, tmp_num):

    global min_num
    global max_num
    
    if(n == N-1):
        min_num = min(tmp_num, min_num)
        max_num = max(tmp_num, max_num)

    if not op[0] == 0:
        op[0]-=1
        calculate(n+1, tmp_num+number[n+1])
        op[0]+=1

    if not op[1] == 0:
        op[1]-=1
        calculate(n+1, tmp_num-number[n+1])
        op[1]+=1

    if not op[2] == 0:
        op[2]-=1
        calculate(n+1, tmp_num*number[n+1])
        op[2]+=1

    if not op[3] == 0:
        op[3]-=1
        calculate(n+1, int(tmp_num/number[n+1]))
        op[3]+=1




calculate(0, number[0])

print(max_num)
print(min_num)



