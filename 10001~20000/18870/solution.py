import sys

def solution(nums):
    numSet = list(set(nums))
    numSet.sort()

    numDict = {}
    for i, n in enumerate(numSet):
        numDict[n] = i
    
    for n in nums:
        sys.stdout.write('%d '%numDict[n])

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    nums = [int(n) for n in sys.stdin.readline().split(' ')]

    solution(nums)