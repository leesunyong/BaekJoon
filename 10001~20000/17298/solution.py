import sys

def solution(N, nums):
   queueIdx = 0; stackIdx = 1
   answer = []

   while True:
      if nums[queueIdx] < nums[stackIdx]:
         answer.append(nums[stackIdx])
         queueIdx += 1; stackIdx = queueIdx + 1
      else :
         stackIdx += 1

      if stackIdx >= len(nums):
         answer.append(-1)
         queueIdx += 1; stackIdx = queueIdx + 1
      
      if queueIdx >= len(nums) - 1:
         answer.append(-1)
         return answer
   

if __name__ == '__main__':
   # N = int(sys.stdin.readline())
   # nums = list(map(int, sys.stdin.readline().split()))
   N = 1000000
   nums = [1000000 - i for i in range(1000000)]

   sys.stdout.write('%s\n'%' '.join([str(c) for c in solution(N, nums)]))