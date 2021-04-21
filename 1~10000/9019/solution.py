import sys
from collections import deque

def solution(T):
    table = [[(i * 2) % 10000, (i + 9999) % 10000, (i % 1000) * 10 + i // 1000, (i % 10) * 1000 + i // 10] for i in range(10000)]
    nextCom = ['D', 'S', 'L', 'R']

    for A, B in T:
        queue = deque(); queue.append(A)
        prevNum = [-1 for _ in range(10000)]; prevNum[A] = A
        prevCom = [-1 for _ in range(10000)]

        while queue:
            current = queue.popleft()

            nextNum = table[current]

            for i, n in enumerate(nextNum):
                if prevNum[n] == -1:
                    prevNum[n], prevCom[n] = current, i
                    queue.append(n)
                    if n == B:
                        queue.clear()
                        break
        
        prevN, prevC = prevNum[B], prevCom[B]; answer = ''
        while prevC != -1:
            answer = nextCom[prevC] + answer
            prevN, prevC = prevNum[prevN], prevCom[prevN]
        sys.stdout.write('%s\n'%answer)
        

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    testCase = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    solution(testCase)