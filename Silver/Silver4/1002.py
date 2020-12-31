import math

N = int(input())

test_cases = []
for i in range(N):
    test_cases.append(input().split(' ')[:6])

for case in test_cases:
    line1 = math.sqrt((int(case[3]) - int(case[0])) ** 2 + (int(case[4]) - int(case[1])) ** 2)
    line2 = int(case[2])
    line3 = int(case[5])

    if line1 == 0 and line2 == line3:
        print(-1)
    elif line1 == line2 + line3 or line2 == line1 + line3 or line3 == line1 + line2:
        print(1)
    elif line1 > line2 + line3 or line2 > line1 + line3 or line3 > line1 + line2:
        print(0)
    else:
        print(2)