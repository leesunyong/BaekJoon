import sys

def solution(clothes):
    closet = {}
    for c in clothes:
        if c[1] in closet.keys():
            closet[c[1]] += 1
        else :
            closet[c[1]] = 1

    answer = 1
    for c in closet:
        answer *= closet[c] + 1 

    return answer - 1

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        clothes = []
        for j in range(N):
            clothes.append(sys.stdin.readline()[:-1].split(' '))
        sys.stdout.write(str(solution(clothes)) + '\n')