def solution(N, houses):
    numHouses = []
    cnt = 0

    for i in range(N):
        for j in range(N):
            if houses[i][j] == '1':
                numHouses.append(0)
                cnt += 1
                queue = [(i, j)]
                houses[i][j] = '0'

                while queue:
                    x, y = queue[0]
                    numHouses[cnt - 1] += 1
                    del queue[0]

                    if x != 0 and houses[x-1][y] == '1':
                        queue.append((x-1, y))
                        houses[x-1][y] = '0'
                    if y != 0 and houses[x][y-1] == '1':
                        queue.append((x, y-1))
                        houses[x][y-1] = '0'
                    if x < N - 1 and houses[x+1][y] == '1':
                        queue.append((x+1, y))
                        houses[x+1][y] = '0'
                    if y < N - 1 and houses[x][y+1] == '1':
                        queue.append((x, y+1))
                        houses[x][y+1] = '0'

    print(cnt)
    numHouses.sort()
    for n in numHouses:
        print(n)

if __name__ == '__main__':
    N = int(input())
    houses = []
    for _ in range(N):
        line = input()
        houses.append(list(line))

    solution(N, houses)