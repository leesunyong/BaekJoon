def solution(N, triangle):
    result = [0 for _ in range(N)]

    result[0] = triangle[0][0]
    for i in range(1, N):
        tmpResult = [0 for _ in range(i + 1)]
        tmpResult[0] = result[0] + triangle[i][0]
        for j in range(1, i):
            if result[j] > result[j-1]:
                tmpResult[j] += result[j]
            else :
                tmpResult[j] += result[j-1]
            tmpResult[j] += triangle[i][j]

        tmpResult[i] = result[i - 1] + triangle[i][i]

        result = tmpResult
    
    return max(result)

if __name__ == '__main__':
    N = int(input())
    triangle = []
    for _ in range(N):
        line = [int(p) for p in input().split(' ')]
        triangle.append(line)

    print(solution(N, triangle))