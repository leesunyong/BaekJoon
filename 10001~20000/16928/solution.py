import sys

def solution(ledder, sneak):
    move = [i for i in range(101)]
    for l in ledder : move[l[0]] = l[1]
    for s in sneak : move[s[0]] = s[1]

    queue = [[move[1 + i], 1] for i in range(1, 7)]
    while len(queue):
        current = queue[0]
        del queue[0]

        for i in range(6, 0, -1):
            if current[0] + i >= 100:
                return current[1] + 1
            elif move[current[0] + i] != current[0] + i:
                queue.append([move[current[0] + i], current[1] + 1])
        
        for i in range(6, 0, -1):
            if move[current[0] + i] == current[0] + i:
                queue.append([move[current[0] + i], current[1] + 1])
                break

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')[:2]]
    ledder = [[int(n) for n in sys.stdin.readline().split(' ')[:2]] for _ in range(N)]
    sneak = [[int(n) for n in sys.stdin.readline().split(' ')[:2]] for _ in range(M)]

    sys.stdout.write('%d\n'%solution(ledder, sneak))
