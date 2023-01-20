# https://www.codetree.ai/training-field/frequent-problems/tree-kill-all

# 0위, 1오른, 2아래, 3왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())

# 숲 초기화하기
forest = []
for row in range(n):
    forest.append(list(map(int, input().split())))

kill_spot = (-1, -1)

total_kill_count = 0


def update(spots_to_be_filled):
    for x_y_count in spots_to_be_filled:
        (empty_x, empty_y, number_to_grow_each_spot) = x_y_count
        forest[empty_x][empty_y] += number_to_grow_each_spot


def empty_xys_around_me(current_forest, x, y):
    empty_xys = []
    empty_xys_count = []
    for direction in range(4):
        next_x = x + dxs[direction]
        next_y = y + dys[direction]
        if not (0 <= next_x < n) or not (0 <= next_y < n):  # 내 주변이 알고보니 범위를 벗어나면
            continue

        spot_by_my_side = current_forest[next_x][next_y]
        # 벽이나 제초제가 없는 빈 칸일 때
        if spot_by_my_side == 0 and not (spot_by_my_side == -1 or spot_by_my_side is None):
            empty_xys.append((next_x, next_y))
    current_tree = current_forest[x][y]
    number_to_grow_each_spot = current_tree // len(empty_xys)

    for item in empty_xys:
        (next_x, next_y) = item
        empty_xys_count.append((next_x, next_y, number_to_grow_each_spot))
    return empty_xys_count


def spread_tree_around_me(current_forest, x, y):
    new_forest = list(map(list, current_forest))
    empty_xys = empty_xys_around_me(new_forest, x, y)
    if len(empty_xys) == 0:
        return []
    return empty_xys


def search_tree_around_me(x, y):
    tree_around_me_count = 0
    # 0위, 1오른, 2아래, 3왼
    for direction in range(4):
        next_x = x + dxs[direction]
        next_y = y + dys[direction]
        if not (0 <= next_x < n) or not (0 <= next_y < n):  # 내 주변이 알고보니 범위를 벗어나면
            continue
        tree_by_my_side = forest[next_x][next_y]
        if tree_by_my_side and not (tree_by_my_side == -1 or tree_by_my_side is None):  # 벽이나 제초제가 아닌, 나무가 있는 칸일 때
            tree_around_me_count += 1
    return tree_around_me_count


def forest_grow():
    for x in range(n):
        for y in range(n):
            current_tree = forest[x][y]
            if current_tree == -1 or not current_tree:  # 벽이 있는 칸이거나, 나무가 없는 칸이면
                continue
            tree_around_me_count = search_tree_around_me(x, y)
            forest[x][y] = current_tree + tree_around_me_count


def forest_spread():
    current_forest = list(map(list, forest))
    spots_to_be_filled = []
    for x in range(n):
        for y in range(n):
            current_tree = current_forest[x][y]
            if current_tree == -1 or not current_tree:  # 벽이 있는 칸이거나, 나무가 없는 칸이면
                continue
            spots_to_be_filled += spread_tree_around_me(current_forest, x, y)
    update(spots_to_be_filled)
    # print(forest)


def simulate_kill_count(x, y):
    # 해당 칸에 제초제를 뿌릴 경우 죽는 나무의 수 계산해 튜플 리턴하기
    # return x, y, simulated_kill_count
    pass


def mark_kill_spot(kill_spot):
    (x, y) = kill_spot
    pass


def kill(kill_spot):
    # 제초제 길이만큼 대각선 다 없애고 제초제 있다고 마킹해주기
    mark_kill_spot(kill_spot)
    pass


for i in range(m):
    if c > 0 and kill_spot != (-1, -1):
        mark_kill_spot(kill_spot)
    # 나무의 성장
    forest_grow()
    # 나무의 번식
    forest_spread()

    # 칸마다 미리 계산해봐서 제초제를 뿌릴 위치 선정하기
    simulated_kill_counts = []
    for x in range(n):
        for y in range(n):
            simulated_kill_counts.append(simulate_kill_count(x, y))

    x, y, simulated_kill_count = max(simulated_kill_counts)
    kill_spot = (x, y)
    kill(kill_spot)

    total_kill_count += simulated_kill_count
    c -= 1

# 이거까지 구현하기까지 약 3시간 반 소요
