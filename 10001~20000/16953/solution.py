import sys

def solution(A, B):
    num = B; cnt = 0
    while num > A:
        cnt += 1
        if num % 2 == 0:
            num //= 2
        elif num % 10 == 1:
            num //= 10
        else : break
        
        
    if num == A: return cnt + 1
    
    return -1

if __name__ == '__main__':
     A, B = map(int, sys.stdin.readline().split())
     sys.stdout.write('%d\n'%solution(A, B))