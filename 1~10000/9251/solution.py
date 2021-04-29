import sys

def solution(s1, s2):
    dp1 = [0 for _ in range(len(s1))]
    dp2 = [0 for _ in range(len(s2))]

    idx2 = 0
    cnt = 0
    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2[:idx2]):
            if c1 == c2:
                idx2 = j
                dp2[j] = dp2[j-1]


    return max(dp2)

if __name__ == '__main__':
    s1 = sys.stdin.readline()[:-1]
    s2 = sys.stdin.readline()[:-1]

    sys.stdout.write('%d\n'%solution(s1, s2))