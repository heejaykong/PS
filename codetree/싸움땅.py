# https://www.codetree.ai/training-field/frequent-problems/battle-ground

# 0:위, 1:오른, 2:아래, 3:왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# n은 격자의 크기, m은 플레이어의 수, k는 라운드의 수를 의미
n, m, k = map(int, input().split())

# 무기 입력받기
ground = [[[] for cell in range(n)] for row in range(n)]
for row in ground:
    guns_per_row = list(map(int, input().split()))
    for i, gun in enumerate(guns_per_row):
        row[i].append(gun)

# 플레이어 입력받기
players = []
for i, _ in enumerate(range(m)):
    # 0:no, 1:x, 2:y, 3:dir, 4:skill, 5:gun, 6:point
    x, y, d, s = list(map(int, input().split()))
    player = [i, x - 1, y - 1, d, s, 0, 0]
    players.append(player)


def loser_rotate():
    pass


def drop_gun():
    pass


def switch_gun():
    pass


def update(current_player):
    no, x, y, dir, skill, old_gun, point = current_player
    for i, p in enumerate(players):
        if i == no:
            p = current_player
            break
    # print(players)


def pick_gun(current_player):
    no, x, y, dir, skill, old_gun, point = current_player
    highest_gun = max(ground[x][y])
    if not highest_gun:
        return
    if highest_gun <= old_gun:
        return
    # 나에게 총이 있다면 내려 놓은 뒤 줍기
    if old_gun > 0:
        ground[x][y].append(old_gun)
    current_player[5] = highest_gun
    update(current_player)


def fight(current_player, enemy):
    no1, x1, y1, dir1, skill1, gun1, point1 = current_player
    no2, x2, y2, dir2, skill2, gun2, point2 = enemy
    curr_power = skill1 + gun1
    enemy_power = skill2 + gun2
    if curr_power == enemy_power:
        return current_player if skill1 > skill2 else enemy




def get_collide(current_player):
    no, curr_x, curr_y, dir, skill, gun, point = current_player
    for i, enemy in enumerate(players):
        if i == no:
            continue
        if curr_x == enemy[1] and curr_y == enemy[2]:
            return enemy
    return None


def move(player):
    no, x, y, dir, skill, gun, point = player
    next_x = x + dxs[dir]
    next_y = y + dys[dir]
    player[1] = next_x
    player[2] = next_y
    update(player)


def in_range(x, y, n, dir):
    next_x = x + dxs[dir]
    next_y = y + dys[dir]
    return (0 <= next_x < n) and (0 <= next_y < n)


def simulate():
    for player in players:
        # player = 0:no, 1:x, 2:y, 3:dir, 4:skill, 5:gun, 6:point
        no, x, y, dir, skill, gun, point = player
        # 격자를 벗어나면 방향을 뒤집어 한칸 이동
        if not in_range(x, y, n, dir):
            if dir < 2:
                player[3] = dir + 2
            else:
                player[3] = dir - 2
        move(player)
        enemy = get_collide(player)
        if not enemy:
            pick_gun(player)
        if enemy:
            fight(player, enemy)


for _ in range(k):
    simulate()
