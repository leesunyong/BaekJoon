while True:
    A, B, C = [int(num) for num in input().split(' ')[:3]]
    if A == 0 and B == 0 and C == 0:
        break
    
    squaredLines = [A**2, B**2, C**2]

    if 2 * max(squaredLines) == sum(squaredLines):
        print('right')
    else :
        print('wrong')