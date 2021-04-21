def add(num1, num2):
    if num1[0] == '-' and num2[0] != '-':
        return minus(num2, num1[1:])
    elif num1[0] != '-' and num2[0] == '-':
        return minus(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        return '-' + add(num1[1:], num2[1:])
    else :
        if len(num1) < len(num2) :
            return add(num2, num1)
        
        carry = 0
        answer = ''
        length = len(num1)
        for i in range(len(num2) - 1, length - 1, -1):
            a = num2[i] + num1[i - length] + carry
            if a > 10:
                a -= 10; carry = 1
            else : carry = 0

            answer = str(a) + answer

        if answer[0] == '0':
            return answer[1:]

        return answer

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
        
        answer = ""
        for i in range(len(num1)):
            a = int(num1[len(num1) - 1 - i])
            if i >= len(num2):
                b = 0
            else :
                b = int(num2[len(num2) - 1 - i])
            digit = a - b
            if digit < 0:
                digit += 10
                num1[len(num1) - 2 - i] = str(int(num1[len(num1) - 2 - i]) - 1)
            
            answer = str(digit) + answer

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
        for i in range(len(num1) + 1):
            if i >= len(num1):
                a = 0
            else :
                a = int(num1[len(num1) - 1 - i])
            digit = a * b + carry
            if digit >= 10:
                carry = digit // 10
            
            answer = str(digit) + answer

        for i in range(len(answer)):
            if answer[i] != '0':
                return answer[i:]
        
        return '0'

A = input()
B = input()

print(add(A,B))
print(minus(A,B))
print(multi(A,B))
