import sys

def solution(s):
    idx = 0
    num = ''
    nums = []
    operators = []
    while True:
        if idx == len(s):
            nums.append(int(num))
            break

        if s[idx] == '+' or s[idx] == '-':
            nums.append(int(num))
            operators.append(s[idx])
            num = ''
        
        else : num += s[idx]
        
        idx += 1

    answer = nums[0]

    o = '+'
    for i in range(len(operators)):
        if operators[i] == '-' :
            o = '-'
            answer -= nums[i + 1]
        elif operators[i] == '+' and o == '-':
            answer -= nums[i + 1]
        else :
            answer += nums[i + 1]
            
    return answer

if __name__ == '__main__':
    s = sys.stdin.readline()[:-1]

    sys.stdout.write('%d\n'%solution(s))