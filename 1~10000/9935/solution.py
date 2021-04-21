import sys

def solution(string, explo):
    explo = list(explo)
    length = len(explo)
    idx = length - 1
    stack = [string[i] for i in range(length - 1)]
    while idx < len(string):
        stack.append(string[idx])
        idx += 1

        if stack[-length:] == explo:
            for _ in range(length): stack.pop()


    return ''.join(stack) if stack else 'FRULA'

if __name__ == '__main__':
    string = sys.stdin.readline()[:-1]
    explo = sys.stdin.readline()[:-1]
    sys.stdout.write('%s\n'%solution(string, explo))