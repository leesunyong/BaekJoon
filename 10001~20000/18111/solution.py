import sys

def solution(N, M, B, land):
    answer = [-1, 0]
    landLevel = [0 for _ in range(257)]

    minHeight, maxHeight = 256, 0
    for i in range(M * N):
        landLevel[land[i]] += 1
        if land[i] > maxHeight:
            maxHeight = land[i]
        if land[i] < minHeight:
            minHeight = land[i]
            
    for h in range(minHeight, maxHeight + 1):    
        rest, time = B, 0
        for i in range(256, -1, -1):
            delta = (i - h) * landLevel[i]
            rest += delta
            if rest < 0:
                time = -1
                break

            if delta < 0: time += -delta
            else : time += 2 * delta

        if time != -1 and (answer[0] == -1 or time <= answer[0]):
            answer[0] = time
            if h > answer[1]: answer[1] = h

    return answer

if __name__ == '__main__':
    N, M, B = [int(n) for n in sys.stdin.readline().split(' ')]

    land = []
    for i in range(N):
        land.extend([int(n) for n in sys.stdin.readline().split(' ')])

    answer = solution(N, M, B, land)
    print(answer[0], answer[1])