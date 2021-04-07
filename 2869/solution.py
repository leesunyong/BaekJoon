def solution(A, B, V):
    d = (V - A) // (A - B)
    r = V - d * (A - B)

    while r > 0:
        d += 1
        r -= A

        if r <= 0: break
        
        r += B

    return d

if __name__ == '__main__':
    A, B, V = [int(n) for n in input().split(' ')]
    print(solution(A, B, V))