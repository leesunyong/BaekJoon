word = list(input().upper())
counts = {}
max = 0
max_char = []
for c in word:
    if c not in counts :
        counts[c] = 1
    else :
        counts[c] += 1
    if counts[c] > max:
        max = counts[c]
        max_char = [c]
    elif counts[c] == max:
        max_char.append(c)

if len(max_char) > 1:
    print('?')
else :
    print(max_char[0])