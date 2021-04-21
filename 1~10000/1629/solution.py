import sys

def solution(A, B, C):
    # if B == 1: return A % C
    # else: 
    #     tmp = solution(A, B // 2, C)
    #     if B % 2 == 0: return (tmp * tmp) % C
    #     else : return (tmp * tmp * A) % C

    return pow(A, B, C)

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().split())
    sys.stdout.write('%d\n'%(solution(A, B, C)))