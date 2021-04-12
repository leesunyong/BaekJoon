import sys

def solution(K, N, coins):
    idx = N - 1
    cnt = 0
    while K > 0:
        coin = coins[idx]
        if coin > K: idx -= 1
        else :
            cnt += K // coin
            K -= coin * (K // coin)
            
    return cnt

if __name__ == '__main__':
    N, K = [int(n) for n in sys.stdin.readline().split(' ')]
    coins = [int(sys.stdin.readline()) for _ in range(N)]

    sys.stdout.write('%d\n'%solution(K, N, coins))