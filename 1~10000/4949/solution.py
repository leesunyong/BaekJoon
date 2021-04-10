import sys

def isBalanced(sentence):
    stack = []
    for c in sentence:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(': return False
            else: del stack[-1]
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if len(stack) == 0 or stack[-1] != '[': return False
            else : del stack[-1]

    if not len(stack): return True

    return False

def solution(sentences):
    for s in sentences:
        if isBalanced(s): print('yes')
        else : print('no')

if __name__ == '__main__':
    sentences = []
    while True:
        sentence = sys.stdin.readline()[:-1]
        if sentence == '.': break

        else : sentences.append(sentence)

    solution(sentences)