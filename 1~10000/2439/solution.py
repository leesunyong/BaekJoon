N = int(input())
for i in range(N):
    print(''.join([' '  for _ in range(N - i - 1)]), end = '')
    print(''.join(['*' for _ in range(i+1)]))