def solution(N, cost):
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = [*cost[0]]
    answer = [0, 0, 0]

    for j in range(3):
        dp[1][0] = dp[0][j] + cost[1][0]
        dp[1][1] = dp[0][j] + cost[1][1]
        dp[1][2] = dp[0][j] + cost[1][2]
        dp[1][j] = 1_000_001

        for i in range(2, N):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

        dp[N-1][j] = 1_000_001

        answer[j] = min(dp[N-1])

    return min(answer)

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, cost))