import sys

def solution(N, M, trees):
    maxHeight = max(trees)
    right, left = maxHeight, 1
    answer = 0
    while True:
        cnt = 0
        current = (right + left) // 2

        for c in trees:
            if c > current : cnt += c - current

        if cnt < M:
            right = current - 1
        elif cnt >= M:
            answer = current
            left = current + 1

        if right < left: return answer

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    trees = [int(n) for n in sys.stdin.readline().split(' ')]

    print(solution(N, M, trees))