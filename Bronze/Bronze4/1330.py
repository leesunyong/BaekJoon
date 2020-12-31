A, B = input().split(' ')[:2]
A, B = int(A), int(B)

if A > B:
    print('>')
elif A < B:
    print('<')
else :
    print('==')