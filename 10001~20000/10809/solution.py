import string

word = input()
for a in list(string.ascii_lowercase):
    print(word.find(a), end=' ')
print('')