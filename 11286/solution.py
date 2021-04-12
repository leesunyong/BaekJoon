import sys

def solution(N, nums):
    maxHeap = [sys.maxsize for _ in range(2 * N + 1)]
    count = 0

    for n in nums:
        if n < 0 : n = n * -2
        elif n > 0: n = n * 2 + 1

        if n == 0:
            if count == 0: sys.stdout.write('0\n')
            else :
                maxValue = maxHeap[1]
                if maxValue % 2 == 0: maxValue //= -2
                else : maxValue = (maxValue - 1) // 2
                sys.stdout.write('%d\n'%maxValue)

                maxHeap[1] = maxHeap[count]
                maxHeap[count] = sys.maxsize

                idx = 1
                while maxHeap[idx] > maxHeap[idx * 2] or maxHeap[idx] > maxHeap[idx * 2 + 1]:
                    if maxHeap[idx * 2 + 1] > maxHeap[idx * 2]:
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
            while idx > 1 and maxHeap[idx // 2] > maxHeap[idx]:
                maxHeap[idx], maxHeap[idx // 2] = maxHeap[idx // 2], maxHeap[idx]
                idx //= 2

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(N)]

    solution(N, nums)