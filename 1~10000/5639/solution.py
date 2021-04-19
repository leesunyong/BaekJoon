import sys

sys.setrecursionlimit(10 ** 6)

def solution(node, left, right):
    idx = right; root = node[left]
    for i in range(left + 1, right):
        if node[i] > root:
            idx = i
            break
    
    if idx > left + 1: solution(node, left + 1, idx)
    if idx < right: solution(node, idx, right)
    sys.stdout.write('%d\n'%root)

if __name__ == '__main__':
    node = []

    while True:
        try :
            node.append(int(sys.stdin.readline()))
        except :
            break
    
    solution(node, 0, len(node))