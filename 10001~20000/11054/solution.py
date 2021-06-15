import sys
import bisect

def bitonic(A, idx, n, reversed=False):
    stack = []
    start, end, order = 0, idx, 1

    if reversed: start, end, order = len(A) - 1, idx, -1

    for i in range(start, end, order):
        
        a = A[i]
        
        if a < n:
            if len(stack) == 0 or stack[-1] < a:
                stack.append(a)
            else :
                idx = bisect.bisect(stack, a)
                if idx == 0 or stack[idx-1] < a:
                    stack[idx] = a
                    
    return len(stack)

def solution(N, A):
    
    m = 0

    for i, a in enumerate(A):
        tmp = bitonic(A, i, a) + bitonic(A, i, a, True) + 1
        if tmp > m : m = tmp

    return m

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

print(solution(N, A))