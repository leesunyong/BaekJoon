a = input().split(' ')
if a[0] == '':
    del a[0]
if a[len(a) - 1] == '':
    del a[len(a) - 1]
print(len(a))