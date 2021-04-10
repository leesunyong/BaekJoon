import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    setList = [False for _ in range(21)]
    for i in range(N):
        c = sys.stdin.readline().replace('\n', '').split(' ')

        command = c[0]
        if command == 'add':
            x = int(c[1])
            setList[x] = True
        elif command == 'remove':
            x = int(c[1])
            setList[x] = False
        elif command == 'check':
            x = int(c[1])
            if setList[x]: sys.stdout.write('1\n')
            else : sys.stdout.write('0\n')
        elif command == 'toggle':
            x = int(c[1])
            setList[x] = not setList[x]
        elif command == 'all':
            setList = [True for _ in range(21)]
        elif command == 'empty':
            setList = [False for _ in range(21)]