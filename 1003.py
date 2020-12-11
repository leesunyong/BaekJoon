N = int(input())

test_cases = []
for i in range(N):
    test_cases.append(int(input()))

fibonacci = [0, 1, 1, 2]
for i in range(3, 40):
    fibonacci.append(fibonacci[i] + fibonacci[i-1])

for case in test_cases:
    if case == 0:
        print(1, 0)
    else :
        print(fibonacci[case-1], fibonacci[case])