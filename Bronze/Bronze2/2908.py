A, B = input().split(' ')[:2]
A = list(A); B = list(B)
A.reverse(); B.reverse()
A = int(''.join(A))
B = int(''.join(B))

if A > B:
    print(A)
else :
    print(B)