def solve(N, solutions):
    left_tmp = 0; right_tmp = N - 1

    min_value = 4_000_000_000
    left, mid, right = -1, -1, -1

    while right_tmp > left_tmp + 1:
        min_s = 4_000_000_000
        for i in range(left_tmp + 1, right_tmp):
            s = solutions[left_tmp] + solutions[i] + solutions[right_tmp]
            if abs(s) < abs(min_s):
                min_s = s
            
            if abs(s) < abs(min_value):
                min_value = s
                left, mid, right = left_tmp, i, right_tmp

        if min_s < 0: left_tmp += 1
        elif min_s > 0: right_tmp -= 1
        else : return solutions[left], solutions[mid], solutions[right]

    return solutions[left], solutions[mid], solutions[right]

print(*solve(int(input()), sorted(list(map(int, input().split())))))