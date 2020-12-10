summation_ex = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 0]

def summation(num):
    if num < 10:
        return summation_ex[num]
        
    base = 1
    cnt = 0
    
    while num >= base:
        base *= 10
        cnt += 1

    base //= 10
    cnt -= 1

    result = summation_ex[(num // base - 1)] * base
    result += (45 * cnt) * (base // 10) * (num // base)
    result += (num // base) * (num % base + 1) + summation(num % base)

    return result


def solution(num1, num2):
    if num1 > num2:
        return 0
    
    return summation(num2) - summation(num1-1)


if __name__ == '__main__':
    line = input()
    L, U = line.split(' ')

    print(solution(int(L), int(U)))
