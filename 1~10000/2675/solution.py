T = int(input())
testCases = []
for _ in range(T):
    testCases.append(input().split(' '))

for test in testCases:
    for c in test[1]:
        for _ in range(int(test[0])):
            print(c, end='')
    print('')