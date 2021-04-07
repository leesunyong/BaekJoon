def solution(N, K):
    answer = 1
    
    for i in range(N, N - K, -1):
        answer *= i
    for i in range(K, 0, -1):
        answer //= i
    
    return answer

if __name__ == '__main__':
    N, K = [int(n) for n in input().split(' ')]
    print(solution(N, K))