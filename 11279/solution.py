import sys

def solution(N, nums):
    maxHeap = [-1 for _ in range(N + 1)]
    count = 0

    for n in nums:
        if n == 0:
            if count == 0: sys.stdout.write('0\n')
            else :
                sys.stdout.write('%d\n'%maxHeap[1])

                maxHeap[1] = maxHeap[count]
                maxHeap[count] = -1

                idx = 1
                while maxHeap[idx] < maxHeap[idx * 2] or maxHeap[idx] < maxHeap[idx * 2 + 1]:
                    if maxHeap[idx] < maxHeap[idx * 2]:
                        maxHeap[idx], maxHeap[idx * 2] = maxHeap[idx * 2], maxHeap[idx]
                        idx *= 2
                    else :
                        maxHeap[idx], maxHeap[idx * 2 + 1] = maxHeap[idx * 2 + 1], maxHeap[idx]
                        idx = idx * 2 + 1

                    if idx == count - 1: break

                count -= 1
        else :
            count += 1
            maxHeap[count] = n
            idx = count
            while idx > 1 and maxHeap[idx // 2] < maxHeap[idx]:
                maxHeap[idx], maxHeap[idx // 2] = maxHeap[idx // 2], maxHeap[idx]
                idx //= 2

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(N)]

    solution(N, nums)