# DP_피보나치수열로_알아보는_메모이제이션_태뷸레이션.py

# 문제:
# 피보나치 수열이란 이전 두 항의 합이 그 다음 항이 되는 수열을 의미합니다.
# 예를 들어 첫 번째 원 소를 1, 두 번째 원소도 1이라 하면 그 다음 항은 2,3,5,8... 이 됩니다.
# N번째 피보나치 수를 구하는 프로그램을 작성해보세요.

# 답안:
n = int(input())

# 1. 재귀법으로 풀기(memoization, 탑다운 방식)
memo = [-1] * (n+1)
def solution(n):
    if memo[n] != -1:
        return memo[n]

    if n == 1 or n == 2:
        memo[n] = 1
    else:
        memo[n] = solution(n-1) + solution(n-2)
    return memo[n]

# # 2. for문으로 풀기(tabulation, 바텀업 방식)
# def solution(n):
#     dp = [-1] * (n+1)
#     dp[1] = 1
#     dp[2] = 1
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]

print(solution(n))

# # 아래는 기본개념 익히면서 연습한 흔적-------------------------------
# 문제: 1부터 N까지의 곱을 구하는 코드를 작성해보자.
# n = 6

# 답변:
# # 1. for문으로 작성하기
# F=[0] * (n+1)
# F[1] = 1
# for i in range(2, n+1):
#     F[i] = F[i-1] * i
# print(F[n])

# # 2. 재귀로 작성하기
# def F1(n):
#     if n == 1:
#         return 1
#     return F1(n - 1) * n
# print(F1(n))

# # 3. 꼬리재귀로 작성하기(걍 내가 혼자 해본거임)
# def F2(n, accumulated_value):
#     if n == 1:
#         return accumulated_value
#     return F2(n - 1, accumulated_value * (n - 1))
# print(F2(n, n))

# # -----------------------------
# 문제: 피보나치 수열 중 n번째 수를 출력하는 함수를 작성해보자.
# # 1. 피보나치 재귀(memoization):
# #     1, 2 면 1,
# #     그 이외는 다 내 전전과 전을 더한 값
# memo = [0] * (n+1)
# def fibbo1(n):
#     global memo

#     if memo[n] != 0:
#         return memo[n]

#     if n == 1 or n == 2:
#         memo[n] = 1
#         return 1
    
#     memo[n] = fibbo1(n-1) + fibbo1(n-2)
#     return memo[n]

# fibbo1(6)
# print(memo[6])

# # 2. 피보나치 for문(tabulation):
# def fibbo2(n):
#     dp = [0] * (n+1)
#     dp[1] = 1
#     dp[2] = 1

#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
    
#     return dp[n]

# print(fibbo2(n))
