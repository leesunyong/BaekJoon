import sys

def solution(pokemon, questions):
    for q in questions:
        sys.stdout.write(pokemon[q] + '\n')

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    pokemon = {}
    questions = []
    
    for i in range(N):
        p = sys.stdin.readline()[:-1]
        pokemon[p] = str(i + 1)
        pokemon[str(i+1)] = p

    for i in range(M):
        questions.append(sys.stdin.readline()[:-1])

    solution(pokemon, questions)