def one_two_three(num):
    answer = [0, 1, 2, 4]

    for i in range(4, num + 1):
        answer.append(answer[i - 1] + answer[i - 2] + answer[i - 3])

    return answer[num]


T = int(input())

test_case = []
for _ in range(T):
    test_case.append(int(input()))

for t in test_case:
    print(one_two_three(t))