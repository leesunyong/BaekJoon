import sys

def triple(tri):
    l = len(tri)
    for i in range(l):
        tri.append(tri[i] + ' ' + tri[i])
        tri[i] = ' ' * l + tri[i] + ' ' * l

def star(N):
    startTri = ['  *  ', ' * * ', '*****']

    while N > 3:
        triple(startTri)
        N //= 2
    
    return startTri

if __name__ == '__main__':
    N = int(input())
    tri = star(N)
    for t in tri:
        print(''.join(t))