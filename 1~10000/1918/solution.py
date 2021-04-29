import sys

def postfixExpr(s):
    openP = []; i = 0
    while i < len(s):
        if s[i] == '(': openP.append(i)
        elif s[i] == ')':
            idxS = openP.pop(); idxE = i
            s[idxS:idxE + 1] = [postfixExpr(s[idxS + 1: idxE])]
            i -= idxE - idxS
            
        i += 1

    i = 0
    while i < len(s):
        if s[i] == '*' or s[i] == '/':
            s[i - 1: i + 2] = [s[i - 1] + s[i + 1] + s[i]]
        else : i += 1

    i = 0
    while i < len(s):
        if s[i] == '+' or s[i] == '-':
            s[i - 1: i + 2] = [s[i - 1] + s[i + 1] + s[i]]
        else : i += 1
    
    return s[0]

def solution(s):
    s = list(s)
    
    return postfixExpr(s)

if __name__ == '__main__':
    s = sys.stdin.readline()[:-1]
    sys.stdout.write('%s\n'%solution(s))