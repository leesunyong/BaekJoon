import sys

def solution(N, video):
    dx = [0, 0, N // 2, N // 2]
    dy = [0, N // 2, 0, N // 2]

    mark = video[0][0]
    answer = ''
    for v in video:
        for c in v:
            if mark != c:
                for k in range(4):
                    answer += solution(N // 2, [[video[dx[k] + l][dy[k] + m] for m in range(N//2)] for l in range(N//2)])

                return '(' + answer + ')'
    
    return mark

if __name__== '__main__':
    N = int(sys.stdin.readline())
    video = [sys.stdin.readline()[:-1] for _ in range(N)]
    sys.stdout.write(solution(N, video) + '\n')