import sys

def solution(N, strings):
    for s in strings:
        cnt = 0
        for c in s:
            if c == '(': cnt += 1
            else : cnt -= 1

            if cnt < 0 :
                break
        
        if cnt != 0: print('NO')
        elif cnt == 0 : print('YES')

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    strings = []
    for i in range(N):
        strings.append(sys.stdin.readline()[:-1])

    solution(N, strings)