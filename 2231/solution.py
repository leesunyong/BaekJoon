def divideSum(N, digit):
    if digit == 0:
        if N < 20 and N % 2 == 0: return N // 2
        else : return -1
    
    msd = N // (10 ** digit + 1)

    tmp = []
    for i in range(msd - 1, msd + 1):
        if i >= 10:
            tmp.append(-1)
            break
        result = divideSum(N - i * (10 ** digit + 1), digit - 1)
        if result != -1:
            tmp.append(i * (10 ** digit) + result)

    minValue = N
    for t in tmp:
        if t != -1 and t < minValue: minValue = t

    if minValue == N: minValue = -1

    return minValue
    
def solution(N):
    digit = len(str(N)) - 1
    
    answer = divideSum(N, digit)
    if answer == -1:
        return 0
    else :
        return answer

if __name__ == '__main__':
    N = int(input())

    print(solution(N))