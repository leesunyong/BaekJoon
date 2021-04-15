import sys
from collections import deque

def solution(A, B):
    prevNum = [-1 for _ in range(10000)]
    prevCom = ['' for _ in range(10000)]
    queue = deque(); queue.append(A)
    prevNum[A] = A
    digit = [1] * 10 + [10] * 90 + [100] * 900 + [1000] * 9000
    while queue:
        current = queue.popleft()

        nextNum = [(current * 2) % 10000, (current + 9999) % 10000]
        nextCom = ['D', 'S', 'L', 'R']
        if current > 9:
            d = digit[current]
            nextNum.extend([(current % d) * 10 + current // d, (current % 10) * d + current // 10])
        
        for i, n in enumerate(nextNum):
            if prevNum[n] == -1:
                prevNum[n], prevCom[n] = current, nextCom[i]
                if n == B: 
                    prevN, prevC = prevNum[B], prevCom[B]; answer = ''
                    while prevC != '':
                        answer = prevC + answer
                        prevN, prevC = prevNum[prevN], prevCom[prevN]
                    
                    return answer
                queue.append(n)


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        sys.stdout.write('%s\n'%solution(A, B))