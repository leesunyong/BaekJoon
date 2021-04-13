import sys

def solution(N, paper):
    queue = [[N, (0, 0)]]
    minusOneCnt, zeroCnt, plusOneCnt = 0, 0, 0

    while len(queue):
        p = queue[0]; del queue[0]

        length, start = p
        end = (start[0] + length - 1, start[1] + length - 1)
        mark = paper[start[0]][start[1]]

        devided = False
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if mark != paper[i][j]:
                    subLength = length // 3
                    for k in range(3):
                        for l in range(3):
                            queue.append([subLength, (start[0] + k * subLength, start[0] + l * subLength)])
                    
                    devided = True
                    break
            
            if devided: break
        
        if not devided:
            if mark == -1: minusOneCnt += 1
            elif mark == 0: zeroCnt += 1
            else : plusOneCnt += 1
    
    return minusOneCnt, zeroCnt, plusOneCnt

if __name__=='__main__':
    N = int(sys.stdin.readline())
    paper = [[int(n) for n in sys.stdin.readline().split(' ')] for _ in range(N)]
    
    minusOne, zero, plusOne = solution(N, paper)
    sys.stdout.write('%d\n%d\n%d\n'%(minusOne, zero, plusOne))
