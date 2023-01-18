# https://www.codetree.ai/training-field/frequent-problems/tree-kill-all

# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())

# 숲 초기화하기
forest = []
for row in range(n):
    forest.append(list(map(int, input().split())))

kill_spot = (-1, -1)

total_kill_count = 0


def grow():
    # 제초제가 있을경우 없을 경우
    pass


def spread():
    # 제초제가 있을경우 없을 경우
    pass


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
    grow()
    # 나무의 번식
    spread()

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

# 이거까지 구현하기까지 약 1시간 반 소요
