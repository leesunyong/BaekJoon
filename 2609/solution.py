def getGCD(num1, num2):
    if num1 % num2 == 0:
        return num2
    elif num2 % num1 == 0:
        return num1
    elif num1 > num2:
        return getGCD(num2, num1 - num2)
    else :
        return getGCD(num1, num2 - num1)

def getLCM(num1, num2, gcd):
    return num1 * num2 // gcd

def solution(num1, num2):
    gcd = getGCD(num1, num2)
    lcm = getLCM(num1, num2, gcd)

    print(gcd)
    print(lcm)

if __name__ == '__main__':
    num1, num2 = input().split(' ')
    num1, num2 = int(num1), int(num2)

    solution(num1, num2)