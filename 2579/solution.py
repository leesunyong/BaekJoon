import sys

def solution(N, stairs):
    scores = [[0, 0] for _ in range(N + 1)]
    scores[1][1] = stairs[1]
    
    if N >= 2:
        scores[2][0] = scores[1][1] + stairs[2]
        scores[2][1] = stairs[2]

        for i in range(3, N + 1):
            scores[i][0] = scores[i-1][1] + stairs[i]
            scores[i][1] = max(scores[i-2]) + stairs[i]
    
    return max(scores[N])

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    stairs = [0]
    for i in range(N):
        stairs.append(int(sys.stdin.readline()))

    sys.stdout.write(str(solution(N, stairs)) + '\n')