import sys

def search(A, numbers):
    result = {}
    pivot = numbers[0]
    numberSmall, numberBig = [], []
    ASmall, ABig = [], []

    for n in numbers[1:]:
        if n > pivot: numberBig.append(n)
        elif n < pivot: numberSmall.append(n)
    
    result[pivot] = '0'
    for a in A:
        if a > pivot: ABig.append(a)
        elif a < pivot: ASmall.append(a)
        else : result[pivot] = '1'


    if not len(ABig) :
        for n in numberBig: result[n] = '0'
    elif len(numberBig):
        result.update(search(ABig, numberBig))
    
    if not len(ASmall) :
        for n in numberSmall: result[n] = '0'
    elif len(numberSmall):
        result.update(search(ASmall, numberSmall))

    return result
            

def solution(N, M, A, numbers):
    answer = search(A, numbers)

    for n in numbers:
        print(answer[n])

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = [int(a) for a in sys.stdin.readline().split(' ')]
    M = int(sys.stdin.readline())
    numbers = [int(n) for n in sys.stdin.readline().split(' ')]

    solution(N, M, A, numbers)