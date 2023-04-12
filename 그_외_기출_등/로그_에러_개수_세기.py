# 문제:
# 로그인 및 로그아웃 정보들이 담긴 로그 집합이 있다.
# 로그가 특정 조건들을 만족하면 에러를 발생시키기로 약속했다.
# 그 조건들은 다음과 같다.
# 1. 유저가 앞선 로그인 로그가 없는데 로그아웃 로그가 발생할 경우
# 2. 유저가 로그인만 연달아 두 번 이상 한 경우
# 3. 유저가 로그아웃만 연달아 두 번 이상 한 경우
# 4. 로그인만 하고 영원히 로그아웃을 하지 않은 경우
# 위에 작성한 조건들처럼, 로그가 잘못 기록된 사람의 수를 출력해 보자.

# 인풋:
# 주어지는 인풋은 로그의 총 개수를 나타내는 정수값 n과,
# 로그의 정보가 담긴 2차원 배열 logs다.
# 하나의 로그는 [로그인 또는 로그아웃, 사용자 이름, 발생 시간] 형태로 이뤄져 있다.

# 테스트케이스:
# 예를들어 n = 7이고,
# logs = [
#     ['login', 'hannah', '15:00'],
#     ['logout', 'john', '15:01'],
#     ['logout', 'hannah', '15:02'],
#     ['login', 'zoe', '15:03'],
#     ['login', 'jane', '15:05'],
#     ['logout', 'jane', '15:06'],
#     ['login', 'jane', '15:07'],
# ]일 경우, 답은 3이 된다.
import sys
input = sys.stdin.readline
n = int(input())
logs = [list(input().split()) for _ in range(n)]

def sort_logs_by_time(logs):
    logs_with_parsed_time = []
    for [action, user, time] in logs:
        parsed_min, parsed_sec = int(time.split(':')[0]), int(time.split(':')[1])
        parsed_time = parsed_min * 60 + parsed_sec
        log = [action, user, parsed_time]
        logs_with_parsed_time.append(log)

    new_logs = sorted(logs_with_parsed_time, key=lambda x: x[2])
    return new_logs

def solution(n, logs):
    login_users = set()
    logout_users = set()
    error_users = set()
    sorted_logs = sort_logs_by_time(logs)

    for [action, user, time] in sorted_logs:
        if action == 'login':
            # 로그인 기록이 중복된 경우
            if user in login_users:
                error_users.add(user)
                continue
            login_users.add(user)
            logout_users.discard(user)
        elif action == 'logout':
            # 로그인한 적 없는 경우
            if user not in login_users:
                error_users.add(user)
                continue
            # 로그아웃 기록이 중복된 경우
            if user in logout_users:
                error_users.add(user)
                continue
            logout_users.add(user)
            login_users.discard(user)
    # 로그인하고 영원히 로그아웃 안 한 경우
    if len(login_users) > 0:
        for user in login_users:
            error_users.add(user)
    # print(error_users)
    return len(error_users)

print(solution(n, logs))
