def solution(N, people):
    peopleSorted = [[] for _ in range(201)]

    for p in people:
        peopleSorted[p[0]].append(p[1])

    for i, p in enumerate(peopleSorted):
        for person in p:
            print(i, person)

if __name__ == '__main__':
    N = int(input())
    people = []
    for _ in range(N):
        age, name = input().split(' ')
        people.append((int(age), name))

    solution(N, people)