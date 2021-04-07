def solution(number):
    for i in range(len(number)):
        if number[i] != number[len(number) - i - 1]:
            return 'no'
    return 'yes'

if __name__ == '__main__':
    testCase = []
    while True:
        case = input()
        if case == '0':
            break
        
        testCase.append(case)

    for c in testCase:
        print(solution(c))