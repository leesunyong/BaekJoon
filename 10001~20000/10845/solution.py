import sys

def solution(N, commands):
    queue = []
    
    for c in commands:
        command = c[0]
        if command == 'push':
            queue.append(int(c[1]))
        elif command == 'pop':
            if len(queue):
                print(queue[0])
                queue = queue[1:]
            else : print(-1)
        elif command == 'size':
            print(len(queue))
        elif command == 'empty':
            if len(queue): print(0)
            else : print(1)
        elif command == 'front':
            if len(queue): print(queue[0])
            else : print(-1)
        elif command == 'back':
            if len(queue): print(queue[-1])
            else : print(-1)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    commands = []
    for i in range(N):
        commands.append(sys.stdin.readline().replace('\n', '').split(' '))

    solution(N, commands)