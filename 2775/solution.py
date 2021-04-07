def solution(T, testCase):

    apartment = [[i for i in range(1, 15)]]
    for i in range(1, 15):
        floor = [1]
        for j in range(1, 14):
            floor.append(floor[j - 1] + apartment[i - 1][j])
        
        apartment.append(floor)

    for t in testCase:
        print(apartment[t[0]][t[1] - 1])

if __name__ == '__main__':
    T = int(input())
    testCase = []
    
    for _ in range(T):
        k = int(input())
        n = int(input())
        testCase.append((k, n))
    
    solution(T, testCase)