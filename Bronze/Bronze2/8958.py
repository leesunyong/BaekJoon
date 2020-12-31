T = int(input())
testCases = []
for _ in range(T):
    testCases.append(input())

for test in testCases:
    idx = 0; score = 0
    for s in test:
        if s == 'X':
            idx = 0
        elif s == 'O':
            idx += 1
            score += idx
    print(score)