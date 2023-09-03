MAX = 30
T = int(input())
dp = [[0] * MAX for i in range(MAX)]

# init
for i in range(1, MAX):
    dp[i][0] = 1
    dp[i][i] = 1
# print(dp)

for i in range(1, MAX):
    for j in range(1, MAX):
        if dp[i][j]:
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# print(dp)

for _ in range(T):
    n, m = tuple(map(int, input().split()))
    print(dp[m][n])