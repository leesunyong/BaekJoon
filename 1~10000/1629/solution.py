import sys

def solution(A, B, C):
    remains = []; r = 1; idx = 0
    A = A % C
    while True:
        r = (r * A) % C
        try :
            idx = remains.index(r)
            return remains[(B - 1) % (len(remains) - idx) + idx]
        except ValueError:
            remains.append(r)
    

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().split())
    sys.stdout.write('%d\n'%(solution(A, B, C)))