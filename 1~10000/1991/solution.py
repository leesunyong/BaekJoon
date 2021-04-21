import sys

read = sys.stdin.readline

def preorder(tree, prev):
    answer = ''

    child = tree[prev]

    answer += prev
    if child[0] != '.': answer += preorder(tree, child[0])
    if child[1] != '.': answer += preorder(tree, child[1])

    return answer

def inorder(tree, prev):
    answer = ''

    child = tree[prev]

    if child[0] != '.': answer += inorder(tree, child[0])
    answer += prev
    if child[1] != '.': answer += inorder(tree, child[1])

    return answer

def postorder(tree, prev):
    answer = ''

    child = tree[prev]

    if child[0] != '.': answer += postorder(tree, child[0])
    if child[1] != '.': answer += postorder(tree, child[1])
    answer += prev

    return answer


def solution(tree):
    root = 'A'

    sys.stdout.write('%s\n'%preorder(tree, root))
    sys.stdout.write('%s\n'%inorder(tree, root))
    sys.stdout.write('%s\n'%postorder(tree, root))

if __name__ == '__main__':
    N = int(read())
    tree = {}
    for _ in range(N):
        parent, child1, child2 = read().split()
        tree[parent] = (child1, child2)

    solution(tree)
