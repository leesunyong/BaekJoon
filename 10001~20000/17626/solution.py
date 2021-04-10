import sys
import math

def solution(N):
    fourSquares = [1 for _ in range(N + 1)]
    a = int(math.sqrt(N))
    for i in range(a):
        for j in range(i*i + 1, min((i+1)*(i+1), N + 1)):
            cnt = 3
            for k in range(1, i + 1):
                tmp = fourSquares[j - k * k]
                if tmp < cnt: cnt = tmp
            fourSquares[j] = cnt + 1
    
    print(fourSquares)

    return fourSquares[N]
    

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    sys.stdout.write("%d\n"%solution(N))