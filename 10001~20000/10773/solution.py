import sys

if __name__ == '__main__':
    K = int(sys.stdin.readline())
    numbers = [0]
    for i in range(K):
        num = int(sys.stdin.readline())
        if num == 0 : del numbers[-1]
        else : numbers.append(num)

    print(sum(numbers))