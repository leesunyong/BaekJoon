n = int(input())

f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for i in range(len(f), n + 1):
    f.append(f[i-1] + f[i-2])

print(f[n])