N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
ds = [list(map(int, input().split())) for _ in range(M)]

# ↑(0), ↓(1), ←(2), →(3)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

S = N // 2  # 상어의 중심 위치
ans1 = ans2 = ans3 = 0
path = []  # 토네이도 경로 저장용

# 1. 토네이도 경로를 미리 만들어 저장 (1차원화 핵심)
def tornado(sx, sy):
    tdx = [-1, 0, 1, 0]
    tdy = [0, 1, 0, -1]
    d = 0  # 방향
    l = 1  # 이동 거리
    l_n = 0  # 2번 반복 시 거리 증가
    c = 0
    x, y = sx, sy

    while len(path) < N * N - 1:
        x += tdx[d]
        y += tdy[d]
        path.append((y, x))
        c += 1

        if c == l:
            c = 0
            d = (d + 1) % 4
            l_n += 1
            if l_n == 2:
                l_n = 0
                l += 1


# 2. 빈 칸 채우기 (구슬을 앞으로 당기기)
def pull_pan():
    tmp = []
    for y, x in path:
        if pan[y][x] != 0:
            tmp.append(pan[y][x])

    for i in range(len(path)):
        y, x = path[i]
        if i < len(tmp):
            pan[y][x] = tmp[i]
        else:
            pan[y][x] = 0


# 3. 구슬 폭발 함수
def buke_pan():
    global ans1, ans2, ans3
    marbles = []

    # 현재 구슬 리스트 추출
    for y, x in path:
        if pan[y][x] != 0:
            marbles.append(pan[y][x])

    exploded = False
    new_marbles = []
    i = 0

    while i < len(marbles):
        j = i
        while j < len(marbles) and marbles[i] == marbles[j]:
            j += 1

        count = j - i
        number = marbles[i]

        if count >= 4:
            exploded = True
            if number == 1:
                ans1 += count
            elif number == 2:
                ans2 += count
            elif number == 3:
                ans3 += count
        else:
            for k in range(i, j):
                new_marbles.append(marbles[k])

        i = j

    # pan에 다시 반영
    for i in range(len(path)):
        y, x = path[i]
        if i < len(new_marbles):
            pan[y][x] = new_marbles[i]
        else:
            pan[y][x] = 0

    return exploded


# 4. 구슬 변화 함수 (그룹으로 변환: 개수, 번호)
def add_boll():
    marbles = []

    for y, x in path:
        if pan[y][x] != 0:
            marbles.append(pan[y][x])

    new_marbles = []
    i = 0

    while i < len(marbles):
        j = i
        while j < len(marbles) and marbles[i] == marbles[j]:
            j += 1

        count = j - i
        number = marbles[i]
        new_marbles.append(count)
        new_marbles.append(number)

        i = j

    # pan에 다시 반영
    for i in range(len(path)):
        y, x = path[i]
        if i < len(new_marbles):
            pan[y][x] = new_marbles[i]
        else:
            pan[y][x] = 0


# 경로 생성
tornado(S, S)

# 마법 시전 M번
for d, s in ds:
    d -= 1  # 방향 보정

    # 1. 얼음 파편 던지기
    for i in range(1, s + 1):
        nx = S + dx[d] * i
        ny = S + dy[d] * i
        if 0 <= nx < N and 0 <= ny < N:
            pan[ny][nx] = 0

    # 2. 빈칸 채우기
    pull_pan()

    # 3. 구슬 폭발 반복
    while buke_pan():
        pull_pan()

    # 4. 구슬 변화
    add_boll()

# 정답 출력
print(1 * ans1 + 2 * ans2 + 3 * ans3)
