import sys
sys.setrecursionlimit(100000)

def calculation(oriNum):
    answer = [0, 0, 1, 1]
    if oriNum < 4:
        return answer[oriNum]
    for i in range(4, oriNum + 1):
        temp = answer[i - 1] + 1
        if i % 2 == 0 and temp > answer[i // 2] + 1:
            temp = answer[i // 2] + 1
        if i % 3 == 0 and temp > answer[i // 3] + 1:
            temp = answer[i // 3] + 1
        
        answer.append(temp)

    return answer[oriNum]        

    

N = int(input())

print(calculation(N))
