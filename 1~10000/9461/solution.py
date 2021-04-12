import sys

def solution(testCase):
    P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(91)]

    for i in range(10, 101):
        P[i] = P[i-1] + P[i - 5]

    for t in testCase:
        print(P[t])

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    testCase = []
    for _ in range(T):
        testCase.append(int(sys.stdin.readline()))

    solution(testCase)