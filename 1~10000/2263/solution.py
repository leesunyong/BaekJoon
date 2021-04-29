import sys
sys.setrecursionlimit(10 ** 5)

def solution(inorder, inorderStart, postorder, postorderStart, length, position, answer):
    root = postorder[postorderStart + length - 1]; idx = position[root]
    
    answer.append(root)
    newLength = idx - inorderStart
    if newLength > 0:
        solution(inorder, inorderStart, postorder, postorderStart, newLength, position, answer)
    if length - newLength > 1:
        solution(inorder, idx + 1, postorder, postorderStart - inorderStart + idx, length - newLength - 1, position, answer)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder = list(map(int, sys.stdin.readline().split()))

    position = {}
    for idx, i in enumerate(inorder): position[i] = idx
    answer = []
    solution(inorder, 0, postorder, 0, n, position, answer)
    sys.stdout.write('%s\n'%(' '.join([str(a) for a in answer])))