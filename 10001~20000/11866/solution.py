import sys

def solution(N, K):
    josephus = []
    current = K - 1
    circle = [i + 1 for i in range(N)]

    while True:
        josephus.append(circle[current])
        del circle[current]
        
        if not len(circle): break

        current = (current + K - 1) % (len(circle))
    
    print('<%s>'%(', '.join([str(j) for j in josephus])))

if __name__ == '__main__':
    N, K = [int(n) for n in sys.stdin.readline().split(' ')]

    solution(N, K)