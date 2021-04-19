import sys

def solution(k, command):
    doublePriorityQueue = ['' for _ in range(1000000)]
    length = 0

    for c, num in command:
        if c == 'I':
            # Insert Method
            length += 1
            current = num; idx = length
            doublePriorityQueue[idx] = current
            while idx > 1 and\
                (doublePriorityQueue[idx] > doublePriorityQueue[idx // 2] or doublePriorityQueue[idx] > doublePriorityQueue[idx // 2 + 1]):
                if doublePriorityQueue[idx // 2] > doublePriorityQueue[idx // 2 + 1]:
                    doublePriorityQueue[idx], doublePriorityQueue[idx // 2 + 1]\
                        = doublePriorityQueue[idx // 2 + 1], doublePriorityQueue[idx]
                else :
                    doublePriorityQueue[idx], doublePriorityQueue[idx // 2]\
                        = doublePriorityQueue[idx // 2], doublePriorityQueue[idx]
                idx //= 2
            
        else :
            if length > 0:
                length -= 1

                if num == 1:
                    # Delete Maximum Value
                    doublePriorityQueue[1], doublePriorityQueue[length + 1] = doublePriorityQueue[length + 1], ''
                    idx = 1
                    while idx < length and\
                        (doublePriorityQueue[idx] < doublePriorityQueue[idx * 2] or doublePriorityQueue[idx] < doublePriorityQueue[idx * 2 + 1]):
                        if doublePriorityQueue[idx * 2] > doublePriorityQueue[idx * 2 + 1]:
                            doublePriorityQueue[idx], doublePriorityQueue[idx * 2]\
                                = doublePriorityQueue[idx * 2], doublePriorityQueue[idx]
                            idx = idx * 2
                        else :
                            doublePriorityQueue[idx], doublePriorityQueue[idx * 2 + 1]\
                                = doublePriorityQueue[idx * 2 + 1], doublePriorityQueue[idx]
                            idx = idx * 2 + 1

                else :
                    # Delete Minimum Value
                    doublePriorityQueue[length + 1] = ''
        
        print(doublePriorityQueue[1:length + 1])
        
    if length == 0: sys.stdout.write('EMPTY\n')
    else : sys.stdout.write('%d %d\n'%(doublePriorityQueue[1], doublePriorityQueue[length]))
            



if __name__ == '__main__':
    T = int(sys.stdin.readline()) # test case
    for _ in range(T):
        k = int(sys.stdin.readline()) # num of operations
        command = []
        for _ in range(k):
            op, num = sys.stdin.readline().split(' '); num = int(num)
            command.append((op, num))

        solution(k, command)