import sys

def solution(N, commands):
    deque = []
    
    for c in commands:
        command = c[0]
        if command == 'push_front':
            deque = [int(c[1])] + deque
        elif command == 'push_back':
            deque.append(int(c[1]))
        elif command == 'pop_front':
            if len(deque):
                print(deque[0])
                deque = deque[1:]
            else : print(-1)
        elif command == 'pop_back':
            if len(deque):
                print(deque[-1])
                deque = deque[:-1]
            else : print(-1)
        elif command == 'size':
            print(len(deque))
        elif command == 'empty':
            if len(deque): print(0)
            else : print(1)
        elif command == 'front':
            if len(deque): print(deque[0])
            else : print(-1)
        elif command == 'back':
            if len(deque): print(deque[-1])
            else : print(-1)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    commands = []
    for i in range(N):
        commands.append(sys.stdin.readline().replace('\n', '').split(' '))

    solution(N, commands)