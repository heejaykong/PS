def solution(floor, room):
    # 0층 먼저 준비해두기
    floorN = [0] * room
    for n in range(1, room + 1):
        floorN[n - 1] = n

    # 내가 원하는 층까지 누적하면서 더하기(1층에서부터 시작)
    for k in range(1, floor + 1):
        # 두번째 호 수부터 시작하기
        for n in range(1, room):
            floorN[n] += floorN[n - 1]
    return floorN[-1]

T = int(input())
for _ in range(T):
    floor = int(input())
    room = int(input())
    print(solution(floor, room))
