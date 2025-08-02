from collections import deque

def is_in_pan(y, x):
    return 0 <= y < N and 0 <= x < M

N, M = map(int, input().split())
pan = [list(input().strip()) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

coins = []
for y in range(N):
    for x in range(M):
        if pan[y][x] == 'o':
            coins.append((y, x))
            pan[y][x] = '.'

visited = set()
q = deque()
q.append((coins[0], coins[1], 0))
visited.add((coins[0], coins[1]))

while q:
    c1, c2, cnt = q.popleft()
    if cnt >= 10:
        break

    for i in range(4):
        ny1, nx1 = c1[0] + dy[i], c1[1] + dx[i]
        ny2, nx2 = c2[0] + dy[i], c2[1] + dx[i]

        out1 = not is_in_pan(ny1, nx1)
        out2 = not is_in_pan(ny2, nx2)

        if out1 and out2:
            continue
        elif out1 or out2:
            print(cnt + 1)
            exit()

        if not out1 and pan[ny1][nx1] == '#':
            ny1, nx1 = c1
        if not out2 and pan[ny2][nx2] == '#':
            ny2, nx2 = c2

        state = ((ny1, nx1), (ny2, nx2))
        if state not in visited:
            visited.add(state)
            q.append(((ny1, nx1), (ny2, nx2), cnt + 1))

print(-1)
