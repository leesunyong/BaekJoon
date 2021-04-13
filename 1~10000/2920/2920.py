ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]
scores = [int(num) for num in input().split(' ')[:8]]

if scores == ascending:
    print('ascending')
elif scores == descending:
    print('descending')
else :
    print('mixed')