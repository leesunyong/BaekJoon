import sys
sys.setrecursionlimit(10 ** 6)

def add(num1, num2):
    negative = ''
    if num1[0] == '-' and num2[0] != '-':
        return minus(num2, num1[1:])
    elif num1[0] != '-' and num2[0] == '-':
        return minus(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        negative = '-'; num1 = num1[1:]; num2 = num2[1:]
        
    if len(num1) < len(num2) : num1 = '0' * (len(num2) - len(num1)) + num1
    else : num2 = '0' * (len(num1) - len(num2)) + num2
    
    carry = 0; answer = ''
    for i in range(len(num2) - 1, -1, -1):
        a = int(num2[i]) + int(num1[i]) + carry
        if a > 10: a -= 10; carry = 1
        else : carry = 0

        answer = str(a) + answer

    return negative + answer

def minus(num1, num2):
    if num1[0] == '-' and num2[0] != '-':
        return '-' + add(num1[1:], num2)
    elif num1[0] != '-' and num2[0] == '-':
        return add(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        return minus(num2[1:], num1[1:])
    else :
        if len(num1) < len(num2) or (len(num1) == len(num2) and int(num1[0]) < int(num2[0])):
            return '-' + minus(num2, num1)
        else :
            num2 = '0' * (len(num1) - len(num2)) + num2
        
        answer = ""
        carry = 0
        for i in range(len(num1)):
            a = int(num1[i]) - int(num2[i]) + carry
            if a < 0 :
                carry -= 1
                a += 10
            
            answer = str(a) + answer

        for i in range(len(answer)):
            if answer[i] != '0':
                return answer[i:]
        
        return '0'

def multi(num1, num2):
    if num1[0] == '-' and num2[0] != '-':
        return '-' + multi(num1[1:], num2)
    elif num1[0] != '-' and num2[0] == '-':
        return '-' + multi(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        return multi(num1[1:], num2[1:])
    else :
        if len(num2) > 1:
            return add(multi(num1, num2[:-1]) + '0', multi(num1, num2[-1]))
        
        b = int(num2)
        carry = 0
        answer = ""
        for i in range(len(num1) - 1, -1, -1):
            a = int(num1[i]) * b + carry
            carry = a // 10
            a %= 10

            answer = str(a) + answer
        
        if carry != 0: answer = str(carry) + answer

        for i in range(len(answer)):
            if answer[i] != '0':
                return answer[i:]
        
        return '0'


def solution(A, B):
    sys.stdout.write('%s\n'%add(A, B))
    sys.stdout.write('%s\n'%minus(A, B))
    sys.stdout.write('%s\n'%multi(A, B))

if __name__ == '__main__':
    A = sys.stdin.readline()[:-1]
    B = sys.stdin.readline()[:-1]

    solution(A, B)