import sys

def solution(N, commands):
    stack = []
    
    for c in commands:
        command = c[0]
        if command == 'push':
            stack = [int(c[1])] + stack
        elif command == 'pop':
            if len(stack):
                print(stack[0])
                stack = stack[1:]
            else : print(-1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            if len(stack): print(0)
            else : print(1)
        elif command == 'top':
            if len(stack): print(stack[0])
            else : print(-1)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    commands = []
    for i in range(N):
        commands.append(sys.stdin.readline().replace('\n', '').split(' '))

    solution(N, commands)