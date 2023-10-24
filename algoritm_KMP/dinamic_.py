M = 6
N = 4
COINS = [
    [0,   1,   1,   1,   1,   1],
    [0,   0,   0,   0,   0,   1],
    [0,   40,  70,  0,   0,   1],
    [100, 0,   0,   0,   0,   1]
]

dp = [[None] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[0][0] = COINS[0][0]
        elif i == 0:
            dp[0][j] = dp[0][j - 1] + COINS[0][j]
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + COINS[i][0]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + COINS[i][j]
    print(dp[i])