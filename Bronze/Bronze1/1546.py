N = int(input())
scores = [int(score) for score in input().split(' ')[:N]]
print(sum(scores) / len(scores) * 100 / max(scores))