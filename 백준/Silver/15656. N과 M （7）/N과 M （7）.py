n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()

answer = []
i=0

def bt(i):
    if i == m:
        print(*answer)
        return

    for t in range(n):
        answer.append(n_list[t])
        bt(i+1)
        answer.pop()

bt(0)

        

