time = [list(map(int, input().split())) for _ in range(3)]

for t in time:
    s = t[5] - t[2]
    m = t[4] - t[1]
    h = t[3] - t[0]
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1

    print(h, m, s)