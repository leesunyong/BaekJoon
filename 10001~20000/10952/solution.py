while True:
    A, B = [int(num) for num in input().split(' ')]
    if A + B == 0:
        break
    print(A + B)