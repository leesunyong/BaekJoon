import sys

def solution(p, array):
    length = len(array)
    reversed = False
    for f in p:
        if f == 'R':
            reversed = not reversed
        else :
            if length == 0: return 'error'
            length -= 1
            if reversed: del array[-1]
            else : del array[0]                

    if reversed:
        array.reverse()
    
    return '[' + ','.join(array) + ']'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        p = sys.stdin.readline()[:-1]
        n = int(sys.stdin.readline())
        array = sys.stdin.readline()[1:-2].split(',')
        if array[0] == '': array = []
        
        sys.stdout.write('%s\n'%solution(p, array))

