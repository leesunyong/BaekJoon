import sys

def solution(N, numbers):
    stack = []
    answer = []
    for i in range(1, N + 1):
        stack.append(i)
        answer.append('+')
        while stack[-1] == numbers[0]:
            del numbers[0]
            del stack[-1]

            answer.append('-')
            
            if not len(numbers) or not len(stack): break
    
    if len(stack) or len(numbers): sys.stdout.write('NO\n')
    else :
        for i in answer:
            sys.stdout.write('%s\n'%i)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    numbers = []
    for _ in range(N):
        numbers.append(int(sys.stdin.readline()))

    solution(N, numbers)