import sys

def solution(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for idx1 in range(1, len(s1) + 1):
        for idx2 in range(1, len(s2) + 1):
            if s1[idx1 - 1] == s2[idx2 - 1]:
                dp[idx1][idx2] = max(dp[idx1-1][idx2-1] + 1, dp[idx1-1][idx2], dp[idx1][idx2-1])
            else :
                dp[idx1][idx2] = max(dp[idx1-1][idx2-1], dp[idx1-1][idx2], dp[idx1][idx2-1])

    return dp[len(s1)][len(s2)]

if __name__ == '__main__':
    s1 = sys.stdin.readline()[:-1]
    s2 = sys.stdin.readline()[:-1]

    sys.stdout.write('%d\n'%solution(s1, s2))