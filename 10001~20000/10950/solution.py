T = int(input())
testCases = [input().split(' ') for _ in range(T)]

for test in testCases:
    print(int(test[0]) + int(test[1]))