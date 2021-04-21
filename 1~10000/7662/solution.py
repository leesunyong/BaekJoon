import sys

import heapq

def solution(k, command):
    maxHeapQ, minHeapQ = [], []
    deleted = [True for _ in range(1_000_001)]
    for i, c in enumerate(command):
        if c[0] == 'I':
            # Insert number
            heapq.heappush(maxHeapQ, (-c[1], i))
            heapq.heappush(minHeapQ, (c[1], i))
            
            deleted[i] = False

        else :
            # Delete number
            if c[1] == 1:
                # Delete from Max Queue
                while maxHeapQ and deleted[maxHeapQ[0][1]]: heapq.heappop(maxHeapQ) 
                if maxHeapQ:
                    deleted[maxHeapQ[0][1]] = True
                    heapq.heappop(maxHeapQ)
            else :
                # Delete from Min Queue
                while minHeapQ and deleted[minHeapQ[0][1]]: heapq.heappop(minHeapQ)
                if minHeapQ:
                    deleted[minHeapQ[0][1]] = True
                    heapq.heappop(minHeapQ)
                    
    while maxHeapQ and deleted[maxHeapQ[0][1]]: heapq.heappop(maxHeapQ)
    while minHeapQ and deleted[minHeapQ[0][1]]: heapq.heappop(minHeapQ)
    
    sys.stdout.write('%s\n'%(str(-maxHeapQ[0][0]) + ' ' + str(minHeapQ[0][0]) if minHeapQ and maxHeapQ else 'EMPTY'))

if __name__ == '__main__':
    T = int(sys.stdin.readline()) # test case
    for _ in range(T):
        k = int(sys.stdin.readline()) # num of operations
        command = []
        for _ in range(k):
            op, num = sys.stdin.readline().split(' '); num = int(num)
            command.append((op, num))

        solution(k, command)