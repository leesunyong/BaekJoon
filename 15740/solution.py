def add(A, B):
    if len(A) > len(B): B = '0' * (len(A) - len(B)) + B
    elif len(A) < len(B): A = '0' * (len(B) - len(A)) + A

    answer = ''
    carry = 0
    for i in range(len(A) - 1, -1, -1):
        a = int(A[i]) + int(B[i]) + carry
        if a >= 10:
            a -= 10
            carry = 1
        else : carry = 0

        answer = str(a) + answer
    
    if carry == 1: answer = '1' + answer
    
    for i in range(len(answer)):
        if answer[i] != '0':
            break
    
    answer = answer[i:]
    
    return answer

def minus(A, B):
    negative = ''
    if len(B) > len(A):
        A, B = B, A
        negative = '-'
    B = '0' * (len(A) - len(B)) + B

    for i in range(len(A)):
        if B[i] < A[i]: break
        if B[i] > A[i]:
            A, B = B, A
            negative = '-'
            break

    answer = ''
    carry = 0
    for i in range(len(A) - 1, -1, -1):
        a = int(A[i]) - int(B[i]) + carry
        if a < 0:
            a += 10
            carry = -1
        else :
            carry = 0
        answer = str(a) + answer
    
    for i in range(len(answer)):
        if answer[i] != '0':
            break
    
    answer = answer[i:]

    return negative + answer


if __name__ == '__main__':
    A, B = input().split()
    if A[0] == '-' and B[0] == '-':
        print('-' + add(A[1:], B[1:]))
    elif A[0] != '-' and B[0] == '-':
        print(minus(A, B[1:]))
    elif A[0] == '-' and B[0] != '-':
        print(minus(B, A[1:]))
    else :
        print(add(A, B))