import sys

def solution(N, numbers):

    sumValue = 0
    cnt, midValue = 0, -4001
    maxCnt, mostFreqValue = 0, []
    minValue, maxValue = 4001, -4001
    for i, n in enumerate(numbers):
        sumValue += n * (i - 4000)

        cnt += n
        if cnt > N // 2 and midValue == -4001: midValue = i - 4000

        if maxCnt < n:
            maxCnt = n
            mostFreqValue = [i - 4000]
        elif maxCnt == n:
            mostFreqValue.append(i - 4000)

        if n > 0 and minValue > i - 4000:
            minValue = i - 4000
        if n > 0 and i - 4000 > maxValue :
            maxValue = i - 4000
    
    avgValue = sumValue // N
    if sumValue % N > N // 2: avgValue += 1
    print(avgValue)

    print(midValue)
    
    if len(mostFreqValue) > 1 : print(mostFreqValue[1])
    else : print(mostFreqValue[0])
    
    print(maxValue - minValue)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    numbers = [0 for _ in range(8001)]
    for i in range(N):
        numbers[int(sys.stdin.readline()) + 4000] += 1

    solution(N, numbers)