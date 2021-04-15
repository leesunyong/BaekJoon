import sys

def solution(N, command):
    switches = [0 for _ in range(9 * N + 1)]
    switches[1] = (False, (1, N))

    for c in command:
        if c[0] == 0:
            print(c)


if __name__ == '__main__':
    N, M = [int(num) for num in sys.stdin.readline().split(' ')]

    quests = []
    for _ in range(M):
        quests.append([int(n) for n in sys.stdin.readline().split(' ')])

    states = [False for _ in range(N)]

    for q in quests:
        quest = q.split(' ')[:3]
        if quest[0] == '0':
            for i in range(int(quest[1]), int(quest[2]) + 1):
                states[i - 1] = not states[i - 1]
        elif quest[0] == '1':
            print(states[int(quest[1]) - 1: int(quest[2])].count(True))