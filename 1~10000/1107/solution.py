import sys

def solution(N, M, broken):
    if len(str(N)) >= abs(100 - N): return abs(100 - N)
    
    idx = 0
    while True:
        dN = [-idx, idx]
        
        channel = ''
        for i in dN:
            find = False
            if N + i < 0: continue
            for c in str(N + i):
                find = int(c) in broken
                if find: break
            
            if not find:
                channel = str(N + i)
                break

        if N - idx == 100 or N + idx == 100 : return idx
        elif channel == '': idx += 1
        else : return len(channel) + idx


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    broken = []
    if M!= 0: broken = list(map(int, sys.stdin.readline().split()))

    sys.stdout.write('%d\n'%solution(N, M, broken))