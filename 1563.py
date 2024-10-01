import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000
dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]
dp[0][0][0], dp[1][0][1], dp[1][1][0] = 1, 1, 1
for i in range(1, N+1):
    dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
    dp[i][0][1] = dp[i-1][0][0]
    dp[i][0][2] = dp[i-1][0][1]
    dp[i][1][0] = dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2] + dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
    dp[i][1][1] = dp[i-1][1][0]
    dp[i][1][2] = dp[i-1][1][1]
print(sum(list(map(sum, dp[N])))%MOD)
