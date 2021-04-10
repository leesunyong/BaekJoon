def solution(N):
    i = 0
    num = 0
    while i < N:
        num += 1
        if str(num).count('666'):
            i += 1
    
    return num

if __name__ == '__main__':
    N = int(input())
    print(solution(N))