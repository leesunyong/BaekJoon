n = int(input())

answer = [0, 1, 2]

for i in range(3, n + 1):
    answer.append((answer[i - 1] + answer[i - 2]) % 10007)

print(answer[n])