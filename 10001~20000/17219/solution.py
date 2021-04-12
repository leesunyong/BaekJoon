import sys

def solution (sitePassword, site):
    for s in site:
        sys.stdout.write(sitePassword[s] + '\n')

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    sitePassword = {}
    for i in range(N):
        site, password = sys.stdin.readline()[:-1].split(' ')
        sitePassword[site] = password
    
    site = []
    for i in range(M):
        site.append(sys.stdin.readline()[:-1])

    solution(sitePassword, site)