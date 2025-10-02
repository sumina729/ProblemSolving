N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()


#연속이 끊어지는 부분 찾아야함
x = 0
for w in n_list:
    if w <= x+1:
        x += w
    else:
        break

print(x+1)