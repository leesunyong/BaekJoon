import sys

def solution(A, B):
    return A * A - B * B

if __name__ == '__main__':
    A, B = map(int, sys.stdin.readline().split())
    sys.stdout.write('%d\n'%solution(A, B))