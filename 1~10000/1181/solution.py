def solution(N, words):
    for word in words:
        s = list(set(word))
        s.sort()
        for w in s:
            print(w)

if __name__ == '__main__':
    N = int(input())
    words = [[] for _ in range(51)]
    for i in range(N):
        word = input()
        words[len(word)].append(word)

    solution(N, words)