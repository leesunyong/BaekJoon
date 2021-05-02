import sys

def star(N):
    if N == 3:
        sys.stdout.write('  *  \n')
        sys.stdout.write(' * * \n')
        sys.stdout.write('*****\n')
    else :
        N //= 2
        

if __name__ == '__main__':
    N = int(input())
    star(N)