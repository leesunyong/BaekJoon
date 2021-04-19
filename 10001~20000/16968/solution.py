import sys

def solution(ex):
    answer = 1
    c = 26; d = 10

    for e in ex:
        if e == 'c':
            answer *= c
            if c == 26: c = 25
            d = 10
        elif e == 'd':
            answer *= d
            if d == 10: d = 9
            c = 26

    return answer

if __name__ == '__main__':
    ex = sys.stdin.readline()[:-1]
    sys.stdout.write('%d\n'%solution(ex))