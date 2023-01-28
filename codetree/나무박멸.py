# 해답 보고 다시 풀었음
# https://www.codetree.ai/training-field/frequent-problems/tree-kill-all

# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = tuple(map(int, input().split()))

# 3종류의 좌표 초기화
# 1. 나무들을 표시하는 좌표
forest = [[0] * (n + 1)]
for _ in range(n):
    forest.append([0] + list(map(int, input().split())))
# 2. 나무들이 확산할 때 활용하는 좌표(연습장같은개념)
forest_spread = [[0] * (n + 1) for _ in range(n + 1)]
# 3. 현재 제초제를 뿌린 현황을 표현하는 좌표(제초제를 뿌린 위치에, 잔존햇수를 표기)
chemical = [[0] * (n + 1) for _ in range(n + 1)]

answer = 0

# 위, 오른, 아래, 왼 순서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
# 좌측상단, 우측상단, 좌측하단, 우측하단 순서
diag_xs = [-1, -1, 1, 1]
diag_ys = [-1, 1, -1, 1]


def not_in_range(x, y):
    return not (1 <= x <= n and 1 <= y <= n)


def step_1_grow():
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if forest[x][y] <= 0:  # 빈 칸이거나 벽이면
                continue

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not_in_range(nx, ny):  # 격자를 벗어나면
                    continue
                if forest[nx][ny] > 0:  # 인접한 나무가 있으면
                    forest[x][y] += 1


def step_2_spread():
    # 일단 forest_spread 격자를 초기화
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            forest_spread[x][y] = 0

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if forest[x][y] <= 0:  # 빈 칸이거나 벽이면
                continue

            # 주변의 빈 칸 찾기(확산할 곳 찾기)
            blank_count = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not_in_range(nx, ny):  # 격자를 벗어나면
                    continue
                if chemical[nx][ny] > 0:  # 제초제 칸이면
                    continue
                if forest[nx][ny] == 0:  # 빈 칸이면
                    blank_count += 1

            # 빈 칸에 할당량만큼 확산시키기
            if blank_count == 0:
                continue
            portion = forest[x][y] // blank_count
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not_in_range(nx, ny):  # 격자를 벗어나면
                    continue
                if chemical[nx][ny] > 0:  # 제초제 칸이면
                    continue
                if forest[nx][ny] == 0:  # 빈 칸이면
                    forest_spread[nx][ny] += portion

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            forest[x][y] += forest_spread[x][y]
    # print(forest)


def step_3_check_kill_spot():
    max_kill_count = 0
    max_x = 1
    max_y = 1
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if forest[x][y] <= 0:
                continue
            # nx 1
            # ny 1

            # 한 칸의 대각선을 탐색
            check_kill_count = forest[x][y]
            for dx, dy in zip(diag_xs, diag_ys):
                for distance in range(1, k + 1):
                    nx, ny = x + (dx * distance), y + (dy * distance)
                    if not_in_range(nx, ny):
                        break

                    if forest[nx][ny] <= 0:  # 벽이거나 나무가 없으면
                        break
                    check_kill_count += forest[nx][ny]
            # 현재 스팟이 나무를 가장 많이 박멸하는지 max값과 비교
            if max_kill_count < check_kill_count:
                max_kill_count = check_kill_count
                max_x = x
                max_y = y

    global answer
    answer += max_kill_count

    return max_x, max_y


def reduce_chemical_time():
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            chemical[x][y] -= 1
    # print(chemical)


def step_3_kill(max_x, max_y):
    # 제초제 뿌리기~!
    chemical[max_x][max_y] = c
    forest[max_x][max_y] = 0

    for dx, dy in zip(diag_xs, diag_ys):
        for distance in range(1, k + 1):
            nx, ny = max_x + (dx * distance), max_y + (dy * distance)
            if not_in_range(nx, ny):
                break
            # 벽이거나 아무것도 없으면 뿌리고 거기서 끝내라
            if forest[nx][ny] <= 0:
                chemical[nx][ny] = c  # 중요한 실수: 여기서 굳이 forest[nx][ny] = 0를 해서 한참 헤맴
                break
            chemical[nx][ny] = c
            forest[nx][ny] = 0

    # print(forest)
    # print(chemical)


for i in range(m):
    # 1. 나무의 성장
    step_1_grow()
    # 2. 나무의 확산
    step_2_spread()
    # 3-1. 가장 많이 박멸되는 칸 찾기
    max_x, max_y = step_3_check_kill_spot()
    # print(max_x, max_y)
    # 제초제 1년 감소
    reduce_chemical_time()
    # 3-2. 비로소 박멸시키기
    step_3_kill(max_x, max_y)

print(answer)
