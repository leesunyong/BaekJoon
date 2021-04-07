import string

def solution(L, string):
    r = 31
    M = 1234567891
    hash = 0

    for i in range(len(string) - 1, -1, -1):
        a = ord(string[i]) - ord('a') + 1
        hash += a

        if i != 0:
            hash *= r
        
        hash %= M

    return hash

if __name__ == '__main__':
    L = int(input())
    string = input()

    print(solution(L, string))