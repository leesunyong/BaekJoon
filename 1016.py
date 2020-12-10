import math

if __name__ == '__main__':
    line = input()
    prime = [2]

    min_num, max_num = line.split(' ')
    min_num = int(min_num)
    max_num = int(max_num)

    diff = max_num - min_num

    nums = [num for num in range(min_num, max_num + 1)]
    
    for num in range(2, int(math.sqrt(max_num) + 1)):

        r = min_num % (num * num)
        if r != 0:
            r = num * num - r

        if num * num > diff and r + min_num > max_num:
            continue

        for i in range(r, max_num - min_num + 1, num * num):
            nums[i] = -1

    print(len(nums) - nums.count(-1))