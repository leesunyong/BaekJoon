A, B = input().split()

answer = ''

if len(A) > len(B):
    B = '0' * (len(A) - len(B)) + B
else :
    A = '0' * (len(B) - len(A)) + A
    
carry = 0
for i in range(len(A)-1, -1, -1):
    a = int(B[i]) + int(A[i]) + carry
    if a >= 10:
        a -= 10
        carry = 1
    else :
        carry = 0
    
    answer = str(a) + answer

if carry == 1: answer = '1' + answer
print(answer)