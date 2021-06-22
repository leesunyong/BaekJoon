def solution(str1, str2):
    dp = [0] * len(str2)
    s = [''] * len(str2)
    maxIdx = 0

    for c in str1:
        # Compare sub-string of str1 (until character 'c')
        maxDP = 0
        maxStr = ''
        for i in range(len(str2)):
            # the biggest dp value and lcs before index 'i'
            # If the dp value of index i is smaller than maxDP,
            # it means that the lcs doesn't contain i's character of str2
            if maxDP < dp[i]:
                maxDP = dp[i]
                maxStr = s[i]
                maxIdx = i
            # if two characters are identical, change the dp value and lcs
            elif c == str2[i]:
                dp[i] = maxDP + 1
                s[i] = maxStr + c
                maxIdx = i

    print(dp[maxIdx])
    print(s[maxIdx])

# Get two strings
str1, str2 = input(), input()
solution(str1, str2)