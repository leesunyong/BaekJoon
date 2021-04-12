import sys

def solution(N, paper):
    blueCnt, whiteCnt = 0, 0
    color = paper[0][0]
    for p in paper:
        for c in p:
            if c != color:
                N = N // 2
                for i in range(2):
                    for j in range(2):
                        blue, white = solution(N, [[paper[N * i + l][N * j + k] for k in range(N)] for l in range(N)])
                        blueCnt += blue; whiteCnt += white
                
                return blueCnt, whiteCnt
    
    if color == 0: return 1, 0
    else : return 0, 1

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    paper = []
    for _ in range(N):
        paper.append([int(n) for n in sys.stdin.readline().split(' ')])
    
    blue, white = solution(N, paper)
    print(blue)
    print(white)
