T = int(input())
testCases = [input().split(' ') for _ in range(T)]

for test in testCases:
    H = int(test[0]); W = int(test[1])
    customer = int(test[2]) - 1

    print((customer % H + 1) * 100 + (customer // H + 1))