# 해답 보고 다시 푸는 중...


# 격자의 크기 n
# 박멸이 진행되는 년 수 m
# 제초제의 확산 범위 k
# 제초제가 남아있는 년 수 c
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
                if forest[nx][ny] == 0:  # 빈 칸이면
                    blank_count += 1

            # 빈 칸에 할당량만큼 확산시키기
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
    print(forest)


def step_3_check_kill_spot():
    max_kill_count = 0
    max_x = 1
    max_y = 1
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if forest[x][y] <= 0:
                continue

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
                chemical[nx][ny] = c
                forest[nx][ny] = 0
                break
            chemical[nx][ny] = c
            forest[nx][ny] = 0

    print(forest)
    print(chemical)


for i in range(m):
    # 1. 나무의 성장
    step_1_grow()
    # 2. 나무의 확산
    step_2_spread()
    # 3-1. 가장 많이 박멸되는 칸 찾기
    max_x, max_y = step_3_check_kill_spot()
    print(max_x, max_y)
    # 제초제 1년 감소
    reduce_chemical_time()
    # 3-2. 비로소 박멸시키기
    step_3_kill(max_x, max_y)





# # https://www.codetree.ai/training-field/frequent-problems/tree-kill-all

# # 0위, 1오른, 2아래, 3왼
# dxs = [-1, 0, 1, 0]
# dys = [0, 1, 0, -1]

# # 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
# n, m, k, c = map(int, input().split())

# # 숲 초기화하기
# forest = []
# for row in range(n):
#     forest.append(list(map(int, input().split())))

# kill_spot = (-1, -1)

# total_kill_count = 0


# def update(spots_to_be_filled):
#     for x_y_count in spots_to_be_filled:
#         (empty_x, empty_y, number_to_grow_each_spot) = x_y_count
#         forest[empty_x][empty_y] += number_to_grow_each_spot


# def empty_xys_around_me(current_forest, x, y):
#     empty_xys = []
#     empty_xys_count = []
#     for direction in range(4):
#         next_x = x + dxs[direction]
#         next_y = y + dys[direction]
#         if not (0 <= next_x < n) or not (0 <= next_y < n):  # 내 주변이 알고보니 범위를 벗어나면
#             continue

#         spot_by_my_side = current_forest[next_x][next_y]
#         # 벽이나 제초제가 없는 빈 칸일 때
#         if spot_by_my_side == 0 and not (spot_by_my_side == -1 or spot_by_my_side is None):
#             empty_xys.append((next_x, next_y))
#     current_tree = current_forest[x][y]
#     number_to_grow_each_spot = current_tree // len(empty_xys)

#     for item in empty_xys:
#         (next_x, next_y) = item
#         empty_xys_count.append((next_x, next_y, number_to_grow_each_spot))
#     return empty_xys_count


# def spread_tree_around_me(current_forest, x, y):
#     new_forest = list(map(list, current_forest))
#     empty_xys = empty_xys_around_me(new_forest, x, y)
#     if len(empty_xys) == 0:
#         return []
#     return empty_xys


# def search_tree_around_me(x, y):
#     tree_around_me_count = 0
#     # 0위, 1오른, 2아래, 3왼
#     for direction in range(4):
#         next_x = x + dxs[direction]
#         next_y = y + dys[direction]
#         if not (0 <= next_x < n) or not (0 <= next_y < n):  # 내 주변이 알고보니 범위를 벗어나면
#             continue
#         tree_by_my_side = forest[next_x][next_y]
#         if tree_by_my_side and not (tree_by_my_side == -1 or tree_by_my_side is None):  # 벽이나 제초제가 아닌, 나무가 있는 칸일 때
#             tree_around_me_count += 1
#     return tree_around_me_count


# def forest_grow():
#     for x in range(n):
#         for y in range(n):
#             current_tree = forest[x][y]
#             if current_tree == -1 or not current_tree:  # 벽이 있는 칸이거나, 나무가 없는 칸이면
#                 continue
#             tree_around_me_count = search_tree_around_me(x, y)
#             forest[x][y] = current_tree + tree_around_me_count


# def forest_spread():
#     current_forest = list(map(list, forest))
#     spots_to_be_filled = []
#     for x in range(n):
#         for y in range(n):
#             current_tree = current_forest[x][y]
#             if current_tree == -1 or not current_tree:  # 벽이 있는 칸이거나, 나무가 없는 칸이면
#                 continue
#             spots_to_be_filled += spread_tree_around_me(current_forest, x, y)
#     update(spots_to_be_filled)
#     # print(forest)


# def simulate_kill_count(x, y):
#     # 해당 칸에 제초제를 뿌릴 경우 죽는 나무의 수 계산해 튜플 리턴하기
#     # return x, y, simulated_kill_count
#     pass


# def mark_kill_spot(kill_spot):
#     (x, y) = kill_spot
#     pass


# def kill(kill_spot):
#     # 제초제 길이만큼 대각선 다 없애고 제초제 있다고 마킹해주기
#     mark_kill_spot(kill_spot)
#     pass


# for i in range(m):
#     if c > 0 and kill_spot != (-1, -1):
#         mark_kill_spot(kill_spot)
#     # 나무의 성장
#     forest_grow()
#     # 나무의 번식
#     forest_spread()

#     # 칸마다 미리 계산해봐서 제초제를 뿌릴 위치 선정하기
#     simulated_kill_counts = []
#     for x in range(n):
#         for y in range(n):
#             simulated_kill_counts.append(simulate_kill_count(x, y))

#     x, y, simulated_kill_count = max(simulated_kill_counts)
#     kill_spot = (x, y)
#     kill(kill_spot)

#     total_kill_count += simulated_kill_count
#     c -= 1

# # 이거까지 구현하기까지 약 3시간 반 소요
