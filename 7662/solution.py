import sys
from queue import PriorityQueue

def solution(command):
    length = 0
    maxQue = PriorityQueue()
    minQue = PriorityQueue()

    for c in command:
        if c[0] == 'I':
            length += 1
            maxQue.put(c[1])
            minQue.put(-c[1])
        else :
            if length > 0:
                length -= 1
                if c[1] == 1:
                    maxQue.get()
                else:
                    -minQue.get()

    if length == 0: sys.stdout.write('EMPTY\n')
    else : sys.stdout.write('%d %d\n'%(maxQue.get(), -minQue.get()))


if __name__ == '__main__':
    T = int(sys.stdin.readline()) # test case
    for _ in range(T):
        k = int(sys.stdin.readline()) # num of operations
        command = []
        for _ in range(k):
            op, num = sys.stdin.readline().split(' '); num = int(num)
            command.append((op, num))

        solution(command)