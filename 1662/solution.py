import sys

def solution(compress):
    answer = 0
    cnt = 0
    startIdx = -1
    for i, c in enumerate(compress):
        if c == '(':
            cnt += 1
            if startIdx == -1: startIdx = i
        elif c == ')':
            cnt -= 1
            if cnt == 0:
                answer += solution(compress[i + 1:])
                compress = compress[:i + 1]
                break

    if startIdx == -1: return len(compress)
    else: return len(compress[:startIdx - 1])\
        + int(compress[startIdx - 1]) * solution(compress[startIdx + 1: -1]) + answer


if __name__ == '__main__':
    compress = sys.stdin.readline()[:-1]

    sys.stdout.write('%d\n'%solution(compress))