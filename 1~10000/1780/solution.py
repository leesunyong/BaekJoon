import sys
from collections import deque

def devide(start, N, paper):

    mark =  paper[start[0]][start[1]]
    if N == 1:        
        if mark == -1: return 1, 0, 0
        elif mark == 0: return 0, 1, 0
        else : return 0, 0, 1

    minusOneCnt, zeroCnt, plusOneCnt = 0, 0, 0
    for k in range(3):
        for l in range(3):
            mOne, zero, pOne = devide((start[0] + k * (N // 3), start[1] + l * (N // 3)), N // 3, paper)
            minusOneCnt += mOne; zeroCnt += zero; plusOneCnt += pOne

    if minusOneCnt == 9 and zeroCnt == 0 and plusOneCnt == 0 : return 1, 0, 0
    elif minusOneCnt == 0 and zeroCnt == 9 and plusOneCnt == 0: return 0, 1, 0
    elif minusOneCnt == 0 and zeroCnt == 0 and plusOneCnt == 9: return 0, 0, 1
    else : return minusOneCnt, zeroCnt, plusOneCnt

def solution(N, paper):
    return devide((0, 0), N, paper)

if __name__=='__main__':
    N = int(sys.stdin.readline())
    paper = [[int(n) for n in sys.stdin.readline().split(' ')] for _ in range(N)]
    
    minusOne, zero, plusOne = solution(N, paper)
    sys.stdout.write('%d\n%d\n%d\n'%(minusOne, zero, plusOne))
