while True:
    try:
        A, B = [int(num) for num in input().split(' ')]
        print(A + B)
    except EOFError:
        break
