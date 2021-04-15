x, y, w, h = input().split(' ')[:4]
print(min([int(x), int(y), int(w) - int(x), int(h) - int(y)]))