from collections import deque

S = int(input())

num_list = [[-1 for S in range(10000) ] for S in range(10000)]


que = deque()
que.append([1, 0])
num_list[1][0] = 0

while que:
    n, c = que.popleft()

    cn_list = []
    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    cn_list.append([n, n])

    # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    cn_list.append([n+c, c])

    # 화면에 있는 이모티콘 중 하나를 삭제한다.
    cn_list.append([n-1, c])

    for nn, nc in cn_list:

        if nn == S:
            print(num_list[n][c]+1)
            exit()

        if num_list[nn][nc] == -1:
            num_list[nn][nc] = num_list[n][c]+1
            que.append([nn, nc])


