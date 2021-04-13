max_val = 0
max_idx = -1

for i in range(9):
    num = int(input())
    if num > max_val:
        max_val = num
        max_idx = i + 1

print(max_val)
print(max_idx)