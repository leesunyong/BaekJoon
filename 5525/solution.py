import sys

def solution(N, M, S):
    cnt = 0
    current = 'I'
    length = 0
    for c in S:
        if c == 'I' :
            if current == 'I':
                length += 1
                if length >= N * 2 + 1:
                    cnt += 1
            else :
                length = 1
            current = 'O'
        else :
            if current == 'O':
                current = 'I'
                length += 1
            else :
                length = 0

        
    return cnt

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    S = sys.stdin.readline()[:-1]

    sys.stdout.write('%d\n'%solution(N, M, S))