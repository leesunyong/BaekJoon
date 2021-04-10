import sys

def solution(N, idx, priority):
    turn = 0
    for p in range(9, 0, -1):
        i = 0
        for j, prior in enumerate(priority):
            if p == prior :
                i = j
                turn += 1
                if j == idx: return turn
        idx = (idx - i + N) % N
        priority = priority[i:] + priority[:i]
        

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N, idx = [int(n) for n in sys.stdin.readline().split(' ')]
        priority = [int(n) for n in sys.stdin.readline().split(' ')]

        print(solution(N, idx, priority))