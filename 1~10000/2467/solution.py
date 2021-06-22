def solution(N, solutions):
    left, right = 0, N - 1

    minDiff = 2_000_000_000
    answer = None

    while left < right:
        diff = solutions[left] + solutions[right]
        absDiff = abs(diff)
        if absDiff < minDiff:
            minDiff = absDiff
            answer = (solutions[left], solutions[right])
        
        if diff < 0: left += 1
        elif diff > 0: right -= 1
        else : break
    
    return answer


N = int(input())
solutions = list(map(int, input().split()))

print(*solution(N, solutions))