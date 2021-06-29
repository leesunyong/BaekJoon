def solution(string):

    return min(dp[len(string)-1])

palindrome = input()

print(solution(palindrome))