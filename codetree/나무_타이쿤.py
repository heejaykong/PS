# https://www.codetree.ai/training-field/frequent-problems/tree-tycoon

#     1→  2↗  3↑  4↖  5←  6↙  7↓  8↘
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

# 격자의 크기 n, 리브로수를 키우는 총 년 수 m이 주어집니다.
n, m = tuple(map(int, input().split()))

# 1. 메인 좌표 초기화
tree = [list(map(int, input().split())) for _ in range(n)]

# 2. 영양제 좌표 초기화
medi = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if x in (n - 1, n - 2) and y in (0, 1):
            medi[x][y] = 1

# 3. 영양제 갱신할 연습장 좌표 초기화
medi_add = [[0 for _ in range(n)] for _ in range(n)]


def out_of_range(x, y):
    return not (0 <= x < n and 0 <= y < n)


def reset_xy(x, y):
    # n 초과 값일 땐: x % n값 리턴
    # while 0 이하 값일 땐: x + 5값 리턴
    new_x, new_y = x, y
    while new_x <= 0:
        new_x += 5
    while new_y <= 0:
        new_y += 5
    if x > 5:
        new_x %= n
    if y > 5:
        new_y %= n
    return new_x, new_y


# 주어진 이동 규칙에 따라 영양제 이동
def step1_move(d, p):
    # 이동 방향 d, 이동 칸 수 p
    for x in range(n):
        for y in range(n):
            if medi[x][y] <= 0:  # 영양제가 없는 빈 칸이면
                continue

            # 이 부분이 문제인듯
            # nx, ny = x + (dxs[d] * p), y + (dys[d] * p)
            # if out_of_range(nx, ny):
            #     nx, ny = reset_xy(nx, ny)
            nx = (x + dxs[d] * p + n * p) % n
            ny = (y + dys[d] * p + n * p) % n

            medi_add[nx][ny] = 1  # 연습장에 표기
    # 연습장에서 medi로 옮겨적기
    for x in range(n):
        for y in range(n):
            medi[x][y] = medi_add[x][y]

    # print(medi)
    # print(medi_add)


# 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가
def step2_put_and_grow():
    for x in range(n):
        for y in range(n):
            if medi[x][y] == 1:
                tree[x][y] += 1


# 대각선으로 인접한 높이 1 이상의 리브로수의 개수 만큼 높이가 증가
def step3_search_and_grow():
    for x in range(n):
        for y in range(n):
            if medi[x][y] == 1:
                # 영양제 투입한 나무의 대각선 탐색하기
                cnt = 0
                for d in (1, 3, 5, 7):
                    nx, ny = x + dxs[d], y + dys[d]
                    if out_of_range(nx, ny):  # 격자를 벗어나면 세지 않음
                        continue
                    if tree[nx][ny] > 0:
                        cnt += 1
                tree[x][y] += cnt


# 특수 영양제를 맞은 땅을 제외하고 높이가 2 이상인 리브로수를 높이 2만큼 잘라내고 해당 땅 위에 특수 영양제를 올려줍니다
def step4_cut():
    # (영양제 초기화)
    for x in range(n):
        for y in range(n):
            medi[x][y] = 0

    for x in range(n):
        for y in range(n):
            if medi_add[x][y] == 1:  # 영양제 맞은 땅 제외하고(초기화된 영양제좌표 대신 연습장을 참고해서)
                continue

            if tree[x][y] >= 2:
                tree[x][y] -= 2  # 높이 2만큼 잘라내고
                medi[x][y] = 1  # 그 자리에 영양제 올리기

    # 영양제 연습장도 초기화
    for x in range(n):
        for y in range(n):
            medi_add[x][y] = 0
    # print(tree)
    # print(medi)


# 이동 규칙은 이동 방향 d, 이동 칸 수 p로 주어지고, d는 1번부터 8번까지 각각 → ↗ ↑ ↖ ← ↙ ↓ ↘으로 주어집니다.
for _ in range(m):
    d, p = tuple(map(int, input().split()))

    # 주어진 이동 규칙에 따라 영양제 이동
    step1_move(d - 1, p)
    # 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가
    step2_put_and_grow()
    # 대각선으로 인접한 높이 1 이상의 리브로수의 개수 만큼 높이가 증가
    step3_search_and_grow()
    # 특수 영양제를 맞은 땅을 제외하고 높이가 2 이상인 리브로수를 높이 2만큼 잘라내고 해당 땅 위에 특수 영양제를 올려줍니다
    step4_cut()

ans = 0
for x in range(n):
    for y in range(n):
        ans += tree[x][y]

print(ans)
